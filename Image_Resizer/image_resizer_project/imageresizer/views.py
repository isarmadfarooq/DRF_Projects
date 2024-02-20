from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from PIL import Image
import io
from django.http import HttpResponse
from .serializer import ImageSerializer

class ResizeImageView(APIView):
    def post(self, request, format=None):
        serializer = ImageSerializer(data=request.data)
        if serializer.is_valid():
            image_data = serializer.validated_data['image'].read()
            width_data = serializer.validated_data['width']
            height_data = serializer.validated_data['height']

            custom_filename = request.data.get('filename')

            img = Image.open(io.BytesIO(image_data))
            resize_image = img.resize((width_data, height_data))

            output_stream = io.BytesIO()

            if custom_filename:
                resize_image.save(output_stream, format="JPEG", quality = 90, optimize=True, progressive=True)
                filename = custom_filename
            else:
                resize_image.save(output_stream, format="JPEG")
                filename = "resized_image.jpg"
            output_stream.seek(0)

            response = HttpResponse(output_stream, content_type='image/jpeg')
            response['Content-Disposition'] = 'attachment; filename="{0}"'.format(filename)
            return response
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)