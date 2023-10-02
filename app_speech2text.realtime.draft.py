import gradio as gr
import speech_recognition as sr

def recognize_speech(source):
    # Initialize the recognizer
    recognizer = sr.Recognizer()

    # Open a microphone input stream
    # with sr.Microphone() as source:
    print("Listening...")

    # Adjust for ambient noise
    recognizer.adjust_for_ambient_noise(source)

    # Recognize speech in real-time
    while True:
        try:
            audio = recognizer.listen(source, timeout=5)  # Capture audio for 5 seconds
            text = recognizer.recognize_google(audio, show_all=False)

            if text:
                print("Caption:", text)
        except sr.WaitTimeoutError:
            pass
        except sr.RequestError:
            print("Could not request results; check your network connection")
        except sr.UnknownValueError:
            pass

# Create a Gradio interface
demo = gr.Interface(
    fn=recognize_speech,
    inputs=gr.Audio(source="microphone", streaming=True),
    live=True,
)

# Launch the Gradio web service
if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0",server_port=8080)