import speech_recognition as sr
import pyttsx3

listener = sr.Recognizer()
speaker = pyttsx3.init()
speaker.setProperty('rate', 150)

faq_data = {
    "order": "Place the order.",
    "return": "You can return it from your orders section.",
    "cancel": "Cancel option is available before shipping.",
    "refund": "Refund takes 5 to 7 working days.",
    "damaged": "You can request a replacement for damaged items.",
    "invoice": "You can download it from your order details.",
    "address": "You can change your address before it is shipped.",
    "password": "You can reset your password using the forgot password option.",
    "login": "Try resetting your password or contact support."
}
conversation_log = []

def talk(text):
    print(f"\n AI: {text}")
    speaker.say(text)
    speaker.runAndWait()

def get_answer(msg):
    msg = msg.lower()
    for keyword in faq_data:
        if keyword in msg:
            return faq_data[keyword]
    return "Sorry, I couldn't find the info you need."

def print_summary():
    print("\n Call Summary:")
    if not conversation_log:
        print("No valid conversation recorded.")
        return

    for i, (q, a) in enumerate(conversation_log, 1):
        print(f"\n{i}.")
        print(f"Customer: {q}")
        print(f"AI: {a}")

def start_conversation():
    print("\n AI Call Assistant with ENTER key — Started!")
    print("Press Enter to speak (say 'exit' to end)\n")

    try:
        with sr.Microphone() as source:
            listener.adjust_for_ambient_noise(source)

            while True:
                input("Press Enter to talk... ")

                try:
                    print("Listening...")
                    audio = listener.listen(source, timeout=5)
                    user_input = listener.recognize_google(audio)

                    if "exit" in user_input.lower():
                        talk("Call ended. Thank you!")
                        conversation_log.append((user_input, "Call ended."))
                        break

                    print(f"\n Customer: {user_input}")
                    reply = get_answer(user_input)
                    talk(reply)

                    conversation_log.append((user_input, reply))

                except sr.UnknownValueError:
                    print("Didn't catch that. Please try again.")
                except sr.WaitTimeoutError:
                    print("No voice detected. Try again.")
                except sr.RequestError as e:
                    print("Mic/Speech error:", e)
                    break

    except KeyboardInterrupt:
        print("\n Exited by user (Ctrl+C)")

    except Exception as mic_error:
        print("Microphone error:", mic_error)

    finally:
        print_summary()

if __name__ == "__main__":
    start_conversation()








