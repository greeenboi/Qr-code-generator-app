

#Standard version of qr code generator
#Version 1.0.0 standard release

from tkinter import *
import customtkinter
from PIL import Image
import qrcode
import time

customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("green")

class App(customtkinter.CTk):
    def __init__(self ,*args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )      
        
        self.title("QR-CODE Generator")
        self.geometry(f"{1080}x{720}")
        
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)
        
        #configure images
        self.logo_image=customtkinter.CTkImage(light_image=Image.open("./media/logo.png"),size=(26,26))
        self.home_image=customtkinter.CTkImage(light_image=Image.open("./media/home.png"),size=(30,30))
        self.default_image=customtkinter.CTkImage(light_image=Image.open("./media/default.png"),size=(150,150))
        self.settings_image=customtkinter.CTkImage(dark_image=Image.open("./media/settings.png"),size=(30,30))
        self.send_image=customtkinter.CTkImage(dark_image=Image.open("./media/send.png"),size=(35,35))
        self.download_image=customtkinter.CTkImage(dark_image=Image.open("./media/download.png"),size=(35,35))
        
        
        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(4, weight=1)
        
        #nav frame
        self.home_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Home",
                                                   fg_color="transparent",image=self.home_image, text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"), anchor="w", command=self.home_button_event)
        self.home_button.grid(row=1, column=0, sticky="ew")

        self.settings_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Settings",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.settings_image, anchor="w", command=self.settings_button_event)
        self.settings_button.grid(row=2, column=0, sticky="ew")
        
        self.navigation_frame_label = customtkinter.CTkLabel(self.navigation_frame, text="  Qr-code generator", image=self.logo_image,
                                                             compound="left", font=customtkinter.CTkFont(size=15, weight="bold"))
        self.navigation_frame_label.grid(row=0, column=0, padx=(20,20), pady=20)
        
        #**my socials**
        self.sidebar_button_1 = customtkinter.CTkButton(self.navigation_frame ,text="Github" , command=self.openweb,hover_color=("#1E5128","#1E5128"))
        self.sidebar_button_1.grid(row=5, column=0, padx=(10,10), pady=10)
        self.sidebar_button_2 = customtkinter.CTkButton(self.navigation_frame ,text="Support me", command=self.open1,hover_color=("#1E5128","#1E5128"))
        self.sidebar_button_2.grid(row=6, column=0, padx=(10,10), pady=10)
        #*****
        
        
        self.appearance_mode_var = customtkinter.StringVar(value="Dark")        
        self.appearance_mode_menu = customtkinter.CTkOptionMenu(self.navigation_frame, values=["Light", "Dark", "System"],command=self.change_appearance_mode_event, variable=self.appearance_mode_var)
        self.appearance_mode_menu.grid(row=7, column=0, padx=20, pady=20, sticky="s")
        
        #home frame
        self.home_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.home_frame.grid_columnconfigure(0, weight=1)
        
        self.qr_code_label = customtkinter.CTkLabel(self.home_frame, text="", image=self.default_image)
        self.qr_code_label.grid(row=0, column=0, padx=20, pady=(20,10))
        
             
        #entries and buttons        
        self.entry = customtkinter.CTkEntry(self, placeholder_text="enter")
        self.entry.grid(row=3, column=1, padx=(20, 10), pady=(20, 20), sticky="nsew")
        self.send_button = customtkinter.CTkButton(master=self, fg_color="transparent",text="",image=self.send_image, border_width=2, width=10,text_color=("gray10", "#DCE4EE"),command=self.generate_qr)
        self.send_button.grid(row=3, column=3, padx=(10, 10), pady=(10, 20), sticky="nsew")
        
        self.download_button=customtkinter.CTkButton(master=self,fg_color="transparent",text="",image=self.download_image, border_width=2, width=10,text_color=("gray10", "#DCE4EE"),command=self.download_qr,state="disabled")
        self.download_button.grid(row=3, column=4, padx=(10, 20), pady=(10, 20), sticky="nsew")
        
        #settings frame
        self.settings_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.settings_frame.grid_columnconfigure((0,1,2),weight=1)
        
        #create settings tabview
        
        self.settings_options_frame = customtkinter.CTkFrame(self.settings_frame)
        self.settings_options_frame.grid(row=0, column=1, padx=(10, 20), pady=(30, 10), sticky="nsew")
        
        self.switch_state=customtkinter.StringVar(value="on")
        self.open_img=customtkinter.CTkSwitch(master=self.settings_options_frame, text="Toggle Open QR-code image by default", variable=self.switch_state,onvalue="on",offvalue="off")
        self.open_img.grid(row=0,column=0,padx=(20,20),pady=(20,10))
        
        self.default_name_text=customtkinter.CTkLabel(self.settings_options_frame,text="Default name of image:",anchor="w")
        self.default_name_text.grid(row=1,column=0,padx=(20,10),pady=(10,10))
        self.text=customtkinter.StringVar(value="qrcodega")
        self.default_name=customtkinter.CTkEntry(self.settings_options_frame,textvariable=self.text)
        self.default_name.grid(row=1,column=1,padx=(0,20),pady=(10,10),sticky="ew")
        
        
        
        # select default frame
        self.select_frame_by_name("home")

    def select_frame_by_name(self, name):
        # set button color for selected button
        self.home_button.configure(fg_color=("gray75", "gray25") if name == "home" else "transparent")
        self.settings_button.configure(fg_color=("gray75", "gray25") if name == "settings" else "transparent")        

        # show selected frame
        if name == "home":
            self.home_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.home_frame.grid_forget()
        if name == "settings":
            self.settings_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.settings_frame.grid_forget()
        
    def construct(self):
        string=f"{self.entry.get()}"
        return string
    
    def generate_qr(self):
        
        time.sleep(3)
        data=self.construct()  
        
        self.qr.add_data(f'{data}')
        self.qr.make(fit=True)
        self.download_button.configure(state="normal")
        
    
    def download_qr(self):
        img = self.qr.make_image(fill_color="black", back_color="white")
        img.save(f"{self.default_name.get()}.png")
        new_qr=customtkinter.CTkImage(light_image=Image.open(f"./{self.default_name.get()}.png"),size=(150,150))
        self.qr_code_label.configure(image=new_qr)
        check=self.open_img.get()        
        if (check=="on"):
            self.open_qr()        
        
    def open_qr(self):
        string=f"./{self.default_name.get()}.png"
        i=Image.open(string)
        i.show()
        
    def openweb(self):           
        webbrowser.open("https://github.com/greeenboi") 
    
    def open1(self):
        webbrowser.open("https://github.com/greeenboi")
       
    
    def change_appearance_mode_event(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)
        
    def home_button_event(self):
        self.select_frame_by_name("home")
    def settings_button_event(self):
        self.select_frame_by_name("settings")
        
        

if __name__ == "__main__":
    app = App()
    app.mainloop()

