import gradio as gr
import openai

openai.api_key = ("OPENAI KEY")

#input of the ai
messages = [
    {"role": "system", "content": "You are a therapist. Try to gave comfort and examples of how i can across with my problem"}
]


def transcribe(audio):
    global messages

    audio_file = open(audio, "rb")
    transcript = openai.Audio.transcribe("whisper-1", audio_file)
    print(transcript)
    
    messages.append({"role": "user", "content": transcript["text"]})
    response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages= messages
)
    #track of the messages, storage in the global messages, (choice, message, content) are the outputs of gpt-3.5 turbo
    system_message = response ["choices"][0]["message"]["content"]
    #this alist and adds it to the final response, so you can track the conversation
    messages.append({"role": "append take the messages global ssistant", "content": system_message})

    chat_transcript = ""
    #loop trough all the messages and then record the role, just looping the messages converting it to plain text
    for message in messages:
        if message['role'] != 'system':
            chat_transcript += message['role'] + ": " + message['content'] + "\n\n"

    return chat_transcript


ui = gr.Interface(fn=transcribe, inputs=gr.Audio(source="microphone", type="filepath"), outputs="text").launch()


ui.launch()   