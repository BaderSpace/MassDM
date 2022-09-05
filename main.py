import tkinter
import tkinter.messagebox
import tkinter.filedialog
import customtkinter
from PIL import Image, ImageTk
import webbrowser


customtkinter.set_appearance_mode("System")

customtkinter.set_default_color_theme("blue")


class App(customtkinter.CTk):
    WIDTH = 800
    HEIGHT = 500

    def __init__(self):
        super().__init__()

        self.title("MassDM")
        self.geometry(f"{App.WIDTH}x{App.HEIGHT}")
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        ######################################IMAGES######################################

        self.logo_image = ImageTk.PhotoImage(
            Image.open("./images/logos/MassDM.png"))
        self.discord_logo_image = ImageTk.PhotoImage(Image.open(
            "./images/logos/discord_logo.png").resize((54, 42), Image.Resampling.LANCZOS))
        self.github_logo_image = ImageTk.PhotoImage(
            Image.open("./images/logos/github_logo.png").resize((65, 65), Image.Resampling.LANCZOS))

        ######################################IMAGES!######################################

        ######################################FRAMES######################################

        self.frame_left = customtkinter.CTkFrame(master=self,
                                                 width=200,
                                                 corner_radius=0)

        self.frame_main = customtkinter.CTkFrame(
            master=self, corner_radius=20)

        self.frame_tokens = customtkinter.CTkFrame(
            master=self, corner_radius=20)

        self.frame_proxies = customtkinter.CTkFrame(
            master=self, corner_radius=20)

        self.main_frame = True
        self.tokens_frame = False
        self.proxies_frame = False

        self.frames_switcher()

        ######################################FRAMES######################################

        ######################################ENTRY######################################

        self.main_message_textbox = customtkinter.CTkTextbox(
            master=self.frame_main, width=500, height=200, corner_radius=0)

        ######################################ENTRY!######################################

        ######################################SCROLLBAR######################################

        self.main_message_scrollbar = customtkinter.CTkScrollbar(
            master=self.main_message_textbox, command=self.main_message_textbox.yview)

        ######################################SCROLLBAR!######################################

        ######################################LABEL######################################

        self.logo_label = customtkinter.CTkLabel(master=self.frame_left,
                                                 image=self.logo_image)

        self.version_label = customtkinter.CTkLabel(master=self.frame_left, text="V 0.01",
                                                    text_font=("Roboto Medium", -16, "bold"))

        self.main_message_label = customtkinter.CTkLabel(
            master=self.frame_main, text="Message:", text_font=("Roboto Medium", -20, "bold"), height=24, width=95)

        ######################################LABEL!######################################

        ######################################BUTTON######################################

        self.main_button = customtkinter.CTkButton(
            master=self.frame_left, text="Main", text_font=("Roboto Medium", -20, "bold"), fg_color="#2CA4FF", corner_radius=35, height=45, width=140, hover=False)
        self.tokens_button = customtkinter.CTkButton(
            master=self.frame_left, text="Tokens", text_font=("Roboto Medium", -20, "bold"), fg_color="#575757", corner_radius=35, height=45, width=140, command=self.switch_to_tokens)
        self.proxies_button = customtkinter.CTkButton(
            master=self.frame_left, text="Proxies", text_font=("Roboto Medium", -20, "bold"), fg_color="#575757", corner_radius=35, height=45, width=140, command=self.switch_to_proxies)
        self.discord_button = customtkinter.CTkButton(
            master=self.frame_left, image=self.discord_logo_image, command=self.go_to_discord, text="Contact me", text_font=("Roboto Medium", -16, "bold"), width=54, height=42, fg_color="#2A2D2E", hover=False)
        self.github_button = customtkinter.CTkButton(master=self.frame_left, image=self.github_logo_image, text="Report a bug/\nRequest features",
                                                     text_font=("Roboto Medium", -12, "bold"), command=self.go_to_github, fg_color="#2A2D2E", hover=False)

        ######################################BUTTON!######################################

        ######################################GRIDING######################################

        self.frame_left.grid(row=0, column=0, sticky="nswe")
        self.logo_label.grid(row=1, column=0, pady=20, padx=32)
        self.main_button.grid(row=2, column=0, pady=(28, 0), padx=0)
        self.tokens_button.grid(row=3, column=0, pady=(30, 0), padx=0)
        self.proxies_button.grid(row=4, column=0, pady=(30, 0), padx=0)
        self.discord_button.grid(row=8, column=0, pady=(30, 0), padx=0)
        self.github_button.grid(row=9, column=0, pady=0, padx=0)
        self.version_label.grid(row=10, column=0, pady=(10, 0), padx=0)
        self.main_message_label.grid(
            row=1, column=0, padx=15, pady=(195, 11), sticky="w")
        self.main_message_textbox.grid(row=2, column=0, padx=15)
        self.main_message_scrollbar.grid(row=0, column=1, sticky="ns")

        ######################################GRIDING!######################################

        ######################################CONFIG######################################

        self.frame_left.grid_rowconfigure(0, minsize=10)
        self.frame_left.grid_rowconfigure(5, weight=1)
        self.frame_left.grid_rowconfigure(8, minsize=20)
        self.frame_left.grid_rowconfigure(11, minsize=10)
        self.main_message_textbox.configure(
            yscrollcommand=self.main_message_scrollbar.set)

        ######################################CONFIG!######################################

        ######################################Functions######################################
    def clear_frame(self):
        self.frame_main.grid_forget()
        self.frame_tokens.grid_forget()
        self.frame_proxies.grid_forget()
        pass

    def frames_switcher(self):
        self.clear_frame()
        if self.main_frame:
            self.frame_main.grid(
                row=0, column=1, sticky="nswe", padx=25, pady=20)
        elif self.tokens_frame:
            self.frame_tokens.grid(
                row=0, column=1, sticky="nswe", padx=25, pady=20)
        elif self.proxies_frame:
            self.frame_proxies.grid(
                row=0, column=1, sticky="nswe", padx=25, pady=20)

    def switch_to_main(self):
        self.main_frame = True
        self.tokens_frame = False
        self.proxies_frame = False

        self.frames_switcher()

        self.main_button = customtkinter.CTkButton(
            master=self.frame_left, text="Main", text_font=("Roboto Medium", -20, "bold"), fg_color="#2CA4FF", corner_radius=35, height=45, width=140, hover=False)
        self.tokens_button = customtkinter.CTkButton(
            master=self.frame_left, text="Tokens", text_font=("Roboto Medium", -20, "bold"), fg_color="#575757", corner_radius=35, height=45, width=140, command=self.switch_to_tokens)
        self.proxies_button = customtkinter.CTkButton(
            master=self.frame_left, text="Proxies", text_font=("Roboto Medium", -20, "bold"), fg_color="#575757", corner_radius=35, height=45, width=140, command=self.switch_to_proxies)

        self.main_button.grid(row=2, column=0, pady=(28, 0), padx=0)
        self.tokens_button.grid(row=3, column=0, pady=(30, 0), padx=0)
        self.proxies_button.grid(row=4, column=0, pady=(30, 0), padx=0)

    def switch_to_tokens(self):

        self.main_frame = False
        self.tokens_frame = True
        self.proxies_frame = False

        self.frames_switcher()

        self.main_button = customtkinter.CTkButton(
            master=self.frame_left, text="Main", text_font=("Roboto Medium", -20, "bold"), fg_color="#575757", corner_radius=35, height=45, width=140, command=self.switch_to_main)
        self.tokens_button = customtkinter.CTkButton(
            master=self.frame_left, text="Tokens", text_font=("Roboto Medium", -20, "bold"), fg_color="#2CA4FF", corner_radius=35, height=45, width=140, hover=False)
        self.proxies_button = customtkinter.CTkButton(
            master=self.frame_left, text="Proxies", text_font=("Roboto Medium", -20, "bold"), fg_color="#575757", corner_radius=35, height=45, width=140, command=self.switch_to_proxies)

        self.main_button.grid(row=2, column=0, pady=(28, 0), padx=0)
        self.tokens_button.grid(row=3, column=0, pady=(30, 0), padx=0)
        self.proxies_button.grid(row=4, column=0, pady=(30, 0), padx=0)

    def switch_to_proxies(self):

        self.main_frame = False
        self.tokens_frame = False
        self.proxies_frame = True

        self.frames_switcher()

        self.main_button = customtkinter.CTkButton(
            master=self.frame_left, text="Main", text_font=("Roboto Medium", -20, "bold"), fg_color="#575757", corner_radius=35, height=45, width=140, command=self.switch_to_main)
        self.tokens_button = customtkinter.CTkButton(
            master=self.frame_left, text="Tokens", text_font=("Roboto Medium", -20, "bold"), fg_color="#575757", corner_radius=35, height=45, width=140, command=self.switch_to_tokens)
        self.proxies_button = customtkinter.CTkButton(
            master=self.frame_left, text="Proxies", text_font=("Roboto Medium", -20, "bold"), fg_color="#2CA4FF", corner_radius=35, height=45, width=140, hover=False)

        self.main_button.grid(row=2, column=0, pady=(28, 0), padx=0)
        self.tokens_button.grid(row=3, column=0, pady=(30, 0), padx=0)
        self.proxies_button.grid(row=4, column=0, pady=(30, 0), padx=0)

    def go_to_discord(self):
        webbrowser.open('https://discord.gg/5ykdz7nW')

    def go_to_github(self):
        webbrowser.open('https://github.com/BaderSpace/MassDM')

        ######################################Functions!######################################


App().mainloop()
