from django.http import JsonResponse
from rest_framework.decorators import api_view

from .utils.desx_encryption import DesxEncryption


@api_view(['POST'])
def encrypt(request):
	key1, key2, key3 = request.data['key1'], request.data['key2'], request.data['key3']

	encryptor = DesxEncryption(key1, key2, key3)
	text = encryptor.desx(request.data['text'], decoding=False)

	return JsonResponse({'text': text, 'key1': key1, 'key2': key2, 'key3': key3, 'type': request.data['type'], 'filename': request.data['filename']}, status=200)


@api_view(['POST'])
def decrypt(request):
	key1, key2, key3 = request.data['key1'], request.data['key2'], request.data['key3']

	encryptor = DesxEncryption(key1, key2, key3)
	text = encryptor.desx(request.data['text'], decoding=True)

	return JsonResponse({'text': text, 'key1': key1, 'key2': key2, 'key3': key3, 'type': request.data['type'], 'filename': request.data['filename']}, status=200)
