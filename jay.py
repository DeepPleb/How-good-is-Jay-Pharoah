import os
from deepgram import Deepgram
import asyncio, json
import sys

# Your Deepgram API Key
DEEPGRAM_API_KEY = 'fffff14aa4ecc90da6f276833599552234f44c1b'

# Location of the file you want to transcribe. Should include filename and extension.
# Example of a local file: ../../Audio/life-moves-pretty-fast.wav
# Example of a remote file: https://static.deepgram.com/examples/interview_speech-analytics.wav
FILE = r"C:\Users\Sarthak\OneDrive\Desktop\katt_jay.wav"

# Mimetype for the file you want to transcribe
# Include this line only if transcribing a local file
# Example: audio/wav
MIMETYPE = 'audio/wav'

async def main():

  # Initialize the Deepgram SDK
  deepgram = Deepgram(DEEPGRAM_API_KEY)

  # Check whether requested file is local or remote, and prepare source
  if FILE.startswith('http'):
    # file is remote
    # Set the source
    source = {
      'url': FILE
    }
  else:
    # file is local
    # Open the audio file
    audio = open(FILE, 'rb')

    # Set the source
    source = {
      'buffer': audio,
      'mimetype': MIMETYPE
    }
  
  # Send the audio to Deepgram and get the response
  response = await asyncio.create_task(
    deepgram.transcription.prerecorded(
      source,
      {
        'punctuate': True, 'tier' : 'enhanced', 'diarize': True
              }
    )
  )
  words = response["results"]['channels'][0]['alternatives'][0]['words']
  
  transcript = []
  for j in words:
        transcript.append([j['word'], j['speaker']])

  string = ''
  for i in transcript:
        if i[1] == 0:
            string = string + i[0] + " "

  print("[speaker 0]: " + string)


try:
  # If running in a Jupyter notebook, Jupyter is already running an event loop, so run main with this line instead:
  #await main()
  asyncio.run(main())
except Exception as e:
  exception_type, exception_object, exception_traceback = sys.exc_info()
  line_number = exception_traceback.tb_lineno
  print(f'line {line_number}: {exception_type} - {e}')