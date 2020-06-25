from rest_framework.response import Response
from rest_framework.views import APIView
from .models import RawImage
from PIL import Image
from rest_framework.generics import get_object_or_404


class ImageView(APIView):

    def get(self, request, pk, height=0, width=0):

        try:
            image_pass = (RawImage.objects.get(pk=pk)).image_path.name
        except:
            return Response({"Error": "Wrong primary key"}, status=404)

        image_full_path = 'media/' + image_pass
        image = Image.open(image_full_path)
        w, h = image.size
        if height == 0 and width == 0:
            return Response({"Answer": "raw image file", "Width": w, "Height": h}, image.show())
        elif 9999 > height > 0 and 9999 > width > 0:
            new_size = (width, height)
            resized_image = image.resize(new_size)
            return Response({"Answer": "modified image file", "Width": width, "Height": height,
                             "Raw file width": w, " Raw file height": h}, resized_image.show())
        else:
            return Response({"Error": "Wrong new image size"}, status=404)
