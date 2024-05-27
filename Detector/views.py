from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import requests

class TextProcessingView(APIView):
    def post(self, request, *args, **kwargs):
        try:
            text = request.data.get('text', '')
            # result = self.process_text(input_text)
            url = "https://writer.com/wp-admin/admin-ajax.php"
            payload = 'action=ai_content_detector_v2&inputs='+str(text)
            headers = {
                'Access-Control-Allow-Origin': '*',
                'Content-Type': 'application/x-www-form-urlencoded'
            }
            response = requests.request("POST", url, headers=headers, data=payload)
            return Response({'result': response.json()}, status=status.HTTP_200_OK)
        except:
            return Response({"result": {"score": 0.5,"label": "AI-Generated"}}, status=status.HTTP_200_OK)

