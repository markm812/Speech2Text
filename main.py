from asyncore import poll
import requests
import sys
import time
from api_secret import *

# upload
upload_endpoint = 'https://api.assemblyai.com/v2/upload'
transcribe_endpoint = "https://api.assemblyai.com/v2/transcript"
filename = sys.argv[1]
upload_headers = {'authorization': API_KEY_ASSEMBLY_AI}
def upload():
    def read_file(filename, chunk_size=5242880):
        with open(filename, 'rb') as _file:
            while True:
                data = _file.read(chunk_size)
                if not data:
                    break
                yield data

    response = requests.post(upload_endpoint,
                            headers=upload_headers,
                            data=read_file(filename))

    return response.json()['upload_url']
   

# transcribe
def transcribe(audio_url):
    json = { "audio_url": audio_url }
    headers = {
        "authorization": API_KEY_ASSEMBLY_AI,
        "content-type": "application/json"
    }
    response = requests.post(transcribe_endpoint, json=json, headers=headers)
    return response.json()['id']

# poll
def poll(transcribe_id):
    polling_endpoint = transcribe_endpoint + '/' + transcribe_id
    polling_response = requests.get(polling_endpoint, headers=upload_headers)
    return polling_response.json()

def get_transcribe_result(id): 
    while True:
        polling_response = poll(id)
        if polling_response['status'] == 'completed':
            return polling_response, None
        elif polling_response['status'] == 'error':
            return polling_response,polling_response['error']
        time.sleep(10)    

# save
def save_transcript(transcribe_result, error):
    transcript_filename = './data/' + filename.split(".")[-1] + ".txt"
    with open(transcript_filename, "w") as f:
        f.write(transcribe_result['text'])
    if error is None:
        print("Transcription saved.")
    else:
        print(error)

transcribed_result, error = get_transcribe_result(transcribe(upload()))
save_transcript(transcribed_result, error)