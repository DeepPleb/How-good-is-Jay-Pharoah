# How good is Jay Pharoah

### Jay Pharoah is one of the greatest mimics of all time. He does impressions of The Rock, Kevin Hart, Obama and so many other celebrities. He's so good that sometimes that it's almost indistinguishable.
One of his best impressions is of a comedian called Katt Williams. 

Here's an audio [file](http://sndup.net/bym4) of Jay and Katt on a video call. 
The first half is Katt speaking and the second half (from 0:08) is Jay imitating Katt. I bet you couldn't make out the difference if I didn't tell you. 

In this little experiment if Deepgram's SDK could distinguish between Jay and Katt using the 'Diarization' feature. 


*Diarization is the process of partitioning an input audio stream into homogeneous segments according to the speaker identity.*

## How to use diarization in [Deepgram](https://developers.deepgram.com/documentation/features/diarize/)
```
response = await asyncio.create_task(
deepgram.transcription.prerecorded(
      source,
      {
        'punctuate': True, 'tier' : 'enhanced', 'diarize': True
              }
    )
  )
```

## Here's the result:
![results](https://github.com/DeepPleb/How-good-is-Jay-Pharoah/blob/main/Screenshot_1.png)

Deepgram outputs a JSON with different speaker labels such as Speaker 0, Speaker 1, Speaker 2 etc.Turns out Jay is **so good** that even a highly trained AI couldn't make out the difference, making Jay Pharoah the GOAT of celebrity impressions!
