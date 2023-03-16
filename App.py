import openai, os, sys
import tkinter
import tkinter.messagebox
import customtkinter

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"

#openai.api_key = os.environ['paste_your_api_key_here']
#openai.api_key = 'paste_your_api_key_here' //Não recomendado, mas útil para fins de teste.
openai.api_key = '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'

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # Open AI Configs

        messages = [
            {"role": "system", "content": "You are a helpful assistant."},
        ]

        # configure window
        self.title("Chat GPT Integration")
        self.geometry(f"{1100}x{500}")

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="Chat GPT\n Integration",
                                                 font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=3, padx=20, pady=(20, 10))
        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Tema:", anchor="w")
        self.appearance_mode_label.grid(row=5, column=3, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame,
                                                                       values=["Light", "Dark", "System"],
                                                                       command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=6, column=3, padx=20, pady=(10, 10))
        self.scaling_label = customtkinter.CTkLabel(self.sidebar_frame, text="Escala UI:", anchor="w")
        self.scaling_label.grid(row=7, column=3, padx=20, pady=(10, 0))
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame,
                                                               values=["80%", "90%", "100%", "110%", "120%"],
                                                               command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=8, column=3, padx=20, pady=(10, 20))

        # create main entry and button
        self.question1 = customtkinter.CTkEntry(self, placeholder_text="")
        self.question1.grid(row=3, column=1, columnspan=2, padx=(20, 0), pady=(20, 20), sticky="nsew")
        self.main_button_1 = customtkinter.CTkButton(master=self, border_width=2, command=self.makequestion, text="Enviar")
        self.main_button_1.grid(row=3, column=3, padx=(20, 20), pady=(20, 20), sticky="nsew")

        # create textbox
        self.textbox = customtkinter.CTkTextbox(self, height=500, wrap="word")
        self.textbox.grid(row=0, column="1", columnspan=5, padx=(20, 20), pady=(15, 15), sticky="nsew")

        # set default values
        self.appearance_mode_optionemenu.set("Dark")
        self.scaling_optionemenu.set("100%")

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

    def makequestion(self):
        self.textbox.delete("0.0", "end")
        messages = [
            {"role": "system", "content": "You are a helpful assistant."},
        ]
        message = self.question1.get()
        messages.append(
            {"role": "user", "content": message},
        )
        chat_completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
        )
        answer = chat_completion.choices[0].message.content
        #        label = customtkinter.CTkLabel(master=frame, text=answer)
        #        label.pack(pady=12, padx=10)
        messages.append({"role": "assistant", "content": answer})
        #        label.pack(pady=12, padx=10)
        self.textbox.insert("0.0", "[Chat GPT]: " + answer + "\n\n")
        self.textbox.insert("0.0", "[Você]: " + message + "\n\n")
        self.question1.delete(0, "end")

if __name__ == "__main__":
    app = App()
    app.mainloop()