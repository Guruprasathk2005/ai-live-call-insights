import speech_recognition as sr
import pyttsx3

recognizer = sr.Recognizer()
speaker = pyttsx3.init()
speaker.setProperty('rate', 140)


faq_keywords = {
    "refund": "Refunds are processed within 5 to 7 working days after pickup or cancellation.",
    "return": "You can raise a return request from your ‘My Orders’ section.",
    "cancel": "You can cancel your order before it is shipped from the ‘My Orders’ page.",
    "track": "You can track your order in the ‘My Orders’ section on your account.",
    "invoice": "You can download your invoice from your order details page.",
    "bill": "You can download your invoice from your order details page.",
    "damaged": "We're sorry! You can request a replacement through the ‘My Orders’ section.",
    "broken": "We're sorry! You can request a replacement through the ‘My Orders’ section.",
    "payment": "If money was deducted, it will be automatically refunded within 3–5 business days.",
    "emi": "EMI is available on select cards and high-value products.",
    "order": "You can place an order by adding items to your cart and proceeding to checkout.",
    "hello": "Hello! How can I help you today?",
    "hi": "Hi there! How can I assist you?",
    "who": "I'm your virtual assistant to help with your orders and queries.",
    "thank": "You're welcome! Happy to help.",
    "bye": "Goodbye! Have a great day!",
    "exit": "Goodbye! Thank you for calling."
}

conversation_log = []

def speak(text):
    print("AI:", text)
    speaker.say(text)
    speaker.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
    try:
        user_text = recognizer.recognize_google(audio).lower()
        print("You:", user_text)
        return user_text
    except sr.UnknownValueError:
        return "Sorry, I didn't catch that."

def get_response(user_input):
    matched_responses = []
    for keyword in faq_keywords:
        if keyword in user_input:
            matched_responses.append(faq_keywords[keyword])
    if matched_responses:
        return " ".join(set(matched_responses))
    return "I'm not sure about that, but you can contact customer support for more help."

print("AI Live Call Assistant Ready (Offline).")
print("Press Enter to talk. Say 'bye' or 'exit' to stop.\n")

while True:
    input("Press Enter to start speaking... ")
    user_text = listen()

    if "bye" in user_text or "exit" in user_text:
        response = get_response(user_text)
        speak(response)
        break

    response = get_response(user_text)
    speak(response)
    conversation_log.append(f"You: {user_text}\n AI: {response}\n")

print("\n Call Summary:")
print("-" * 30)
for line in conversation_log:
    print(line)

with open("call_summary.txt", "w", encoding="utf-8") as f:
    f.write(" AI Live Call Summary\n\n")
    f.write("\n".join(conversation_log))

print("\n Summary saved to call_summary.txt")












