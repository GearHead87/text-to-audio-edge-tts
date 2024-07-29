import edge_tts
import asyncio

async def text_to_speech(input_file, output_file, voice='bn-BD-PradeepNeural', rate='+0%'):
    # Read the input text file
    with open(input_file, 'r', encoding='utf-8') as file:
        text = file.read()

    # Initialize the TTS object
    communicate = edge_tts.Communicate(text, voice=voice, rate=rate)

    # Generate the speech and save it to the output file
    await communicate.save(output_file)

# Define the input and output files
input_file = 'test1.txt'
output_file = 'output.mp3'

# Run the text-to-speech function
asyncio.run(text_to_speech(input_file, output_file))
