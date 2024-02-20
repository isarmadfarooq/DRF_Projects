from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Employee,AttendenceRecord
from .serializer import EmployeeSerializer, AttendenceRecordSerializer
import face_recognition
import cv2
import numpy as np
import csv
from  datetime import datetime

@api_view(['POST'])
def mark_attendance(request):
    if request.method == 'POST':
        employees = Employee.objects.all()
        known_face_encodings = []
        known_face_names = []

        for employee in employees:
            image = face_recognition.load_image_file(employee.picture.path)
            encoding = face_recognition.face_encodings(image)[0]
            known_face_encodings.append(encoding)
            known_face_names.append(employee.name)
        
        video_capture = cv2.VideoCapture(0)

        current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        with open("attendance_records.csv", mode='a', newline='') as csvfile:
            writer = csv.writer(csvfile)

            while True:
                ret, frame = video_capture.read()
                rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

                face_locations = face_recognition.face_locations(rgb_frame)
                face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

                for face_encoding, face_location in zip(face_encodings, face_locations):
                    matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
                    name = 'Unknown'

                    if True in matches:
                        first_match_index = matches.index(True)
                        name = known_face_names[first_match_index]

                        writer.writerow([name, current_datetime])
                        AttendenceRecord.objects.create(employee_name=name, time_stamp=current_datetime)

                        font = cv2.FONT_HERSHEY_DUPLEX
                        cv2.putText(frame, name, (face_location[3], face_location[0]), font, 1.0, (255, 255, 255), 1)
                
                cv2.imshow('Video', frame)

                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

        video_capture.release()
        cv2.destroyAllWindows()

        attendance_record = AttendenceRecord.objects.create(employee_name=name, time_stamp=current_datetime)
        serializer = AttendenceRecordSerializer(attendance_record)
        return Response(serializer.data)

    return Response({"message": "Attendance marked successfully"})
