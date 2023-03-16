import customtkinter
import openai, os, sys

openai.api_key = os.environ['api_key']

messages = [
    {"role": "system", "content": "You are a helpful assistant."},
]

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("1024x768")
root.title("Integração com Chat GPT")


def makequestion():
    message = question1.get()
    messages.append(
        {"role": "user", "content": message},
    )
    chat_completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    answer = chat_completion.choices[0].message.content
    label = customtkinter.CTkLabel(master=frame, text=answer)
    label.pack(pady=12, padx=10)
    messages.append({"role": "assistant", "content": answer})
    label.pack(pady=12, padx=10)


frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=40, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text="Faça a sua pergunta")
label.pack(pady=12, padx=5)

question1 = customtkinter.CTkEntry(master=frame, placeholder_text="")
question1.pack(pady=12, padx=10)

button = customtkinter.CTkButton(master=frame, text="Perguntar", command=makequestion)
button.pack(pady=12, padx=10)

root.mainloop()
