import customtkinter
import os
from PIL import Image
import pandas as pd
import numpy as np
from scipy.stats import gmean
from tkinter import filedialog  # Import the file dialog module
from tkinter import messagebox


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("image_example.py")
        self.geometry("1200x650")

        # set grid layout 1x2
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # load images with light and dark mode image
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "test_images")
        self.logo_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "CustomTkinter_logo_single.png")), size=(26, 26))
        self.large_test_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "about.png")), size=(600, 220))
        self.hoogot_test_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "dedede.png")), size=(600, 220))
        self.agebt_test_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "bbb.png")), size=(600, 220))
        self.image_icon_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "image_icon_light.png")), size=(20, 20))
        self.home_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "home_dark.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "home_light.png")), size=(20, 20))
        self.chat_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "chat_dark.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "chat_light.png")), size=(20, 20))
        self.add_user_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "add_user_dark.png")),
                                                     dark_image=Image.open(os.path.join(image_path, "add_user_light.png")), size=(20, 20))

        # create navigation frame
        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(5, weight=1)

        self.navigation_frame_label = customtkinter.CTkLabel(self.navigation_frame, text="  ", image=self.logo_image,
                                                             compound="left", font=customtkinter.CTkFont(size=15, weight="bold"))
        self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)

        self.home_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="о нас",
                                                   fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                   image=self.home_image, anchor="w", command=self.home_button_event)
        self.home_button.grid(row=1, column=0, sticky="ew")

        self.frame_2_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="hooghoudt",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.chat_image, anchor="w", command=self.frame_2_button_event)
        self.frame_2_button.grid(row=2, column=0, sticky="ew")

        self.frame_3_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="2Аверьянов",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.add_user_image, anchor="w", command=self.frame_3_button_event)
        self.frame_3_button.grid(row=3, column=0, sticky="ew")
        
        self.frame_4_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="2Аверьянов",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.add_user_image, anchor="w", command=self.frame_4_button_event)
        self.frame_4_button.grid(row=4, column=0, sticky="ew")

        self.appearance_mode_menu = customtkinter.CTkOptionMenu(self.navigation_frame, values=["Light", "Dark", "System"],
                                                                command=self.change_appearance_mode_event)
        self.appearance_mode_menu.grid(row=6, column=0, padx=20, pady=20, sticky="s")

        # create home frame
        self.home_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.home_frame.grid_columnconfigure(0, weight=1)

        self.home_frame_large_image_label = customtkinter.CTkLabel(self.home_frame, text="", image=self.large_test_image)
        self.home_frame_large_image_label.grid(row=0, column=0, padx=20, pady=10)
        
        self.textbox_home_frame = customtkinter.CTkTextbox(self.home_frame, width=600, height=300)
        self.textbox_home_frame.grid(row=1, column=0, padx=20, pady=10)
        self.textbox_home_frame.insert("1.0", "НИУ МГСУ \n Дмитрий Вячеславович Козлов,профессор,\n доктор технических наук,заведующий кафедрой Гидравлики и гидротехнического строительства НИУ МГСУ")
        self.textbox_home_frame.configure(state='disabled')  # Set the state to DISABLED

        # self.home_frame_button_1 = customtkinter.CTkButton(self.home_frame, text="", image=self.image_icon_image)
        # self.home_frame_button_1.grid(row=1, column=0, padx=20, pady=10)
        # self.home_frame_button_2 = customtkinter.CTkButton(self.home_frame, text="CTkButton", image=self.image_icon_image, compound="right")
        # self.home_frame_button_2.grid(row=2, column=0, padx=20, pady=10)
        # self.home_frame_button_3 = customtkinter.CTkButton(self.home_frame, text="CTkButton", image=self.image_icon_image, compound="top")
        # self.home_frame_button_3.grid(row=3, column=0, padx=20, pady=10)
        # self.home_frame_button_4 = customtkinter.CTkButton(self.home_frame, text="CTkButton", image=self.image_icon_image, compound="bottom", anchor="w")
        # self.home_frame_button_4.grid(row=4, column=0, padx=20, pady=10)

        # create second frame
        self.second_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.second_frame.grid_columnconfigure(0, weight=1)

        self.second_frame_large_image_label = customtkinter.CTkLabel(self.second_frame, text="", image=self.hoogot_test_image,width=600)
        self.second_frame_large_image_label.grid(row=0, column=0, padx=20, pady=10)

        self.second_frame_button_1 = customtkinter.CTkButton(self.second_frame, text="Upload Excel File", image=self.image_icon_image, compound="right",width=600,height=60,command=self.upload_excel_file)
        self.second_frame_button_1.grid(row=2, column=0, padx=20, pady=10)
        self.second_entry1 = customtkinter.CTkEntry(self.second_frame, placeholder_text="Path/To/Excel",width=600,height=50)
        self.second_entry1.grid(row=3, column=0, padx=20, pady=10)
        
        self.second_entry2 = customtkinter.CTkEntry(self.second_frame, placeholder_text="Enter d",width=600,height=35)
        self.second_entry2.grid(row=4, column=0, padx=20, pady=10)
        
        self.second_entry3 = customtkinter.CTkEntry(self.second_frame, placeholder_text="Enter r",width=600,height=35)
        self.second_entry3.grid(row=5, column=0, padx=20, pady=10)
        
        self.second_entry4 = customtkinter.CTkEntry(self.second_frame, placeholder_text="Enter K",width=600,height=35)
        self.second_entry4.grid(row=6, column=0, padx=20, pady=10)
        
        self.second_frame_button_2 = customtkinter.CTkButton(self.second_frame, text="Calculate", image=self.image_icon_image, compound="right",width=600,height=60,command=self.calculate_event1)
        self.second_frame_button_2.grid(row=7, column=0, padx=20, pady=10)
        
        self.textbox_second_frame = customtkinter.CTkTextbox(self.second_frame,width=300,height=60,)
        self.textbox_second_frame.grid(row=2, column=3,padx=20, pady=10)
        
        self.textbox_second_frame2 = customtkinter.CTkTextbox(self.second_frame,width=300,height=60,)
        self.textbox_second_frame2.grid(row=3, column=3,padx=20, pady=10)

        
        # create third frame
        self.third_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.third_frame.grid_columnconfigure(0, weight=1)

        self.third_frame_large_image_label = customtkinter.CTkLabel(self.third_frame, text="", image=self.agebt_test_image,width=600)
        self.third_frame_large_image_label.grid(row=0, column=0, padx=20, pady=10)

        self.third_frame_button_1 = customtkinter.CTkButton(self.third_frame, text="Upload Excel File", image=self.image_icon_image, compound="right",width=600,height=60,command=self.upload_excel_file)
        self.third_frame_button_1.grid(row=2, column=0, padx=20, pady=10)
        self.third_entry1 = customtkinter.CTkEntry(self.third_frame, placeholder_text="Path/To/Excel",width=600,height=50)
        self.third_entry1.grid(row=3, column=0, padx=20, pady=10)
        
        self.third_entry2 = customtkinter.CTkEntry(self.third_frame, placeholder_text="Enter d",width=600,height=35)
        self.third_entry2.grid(row=4, column=0, padx=20, pady=10)
        
        self.third_entry3 = customtkinter.CTkEntry(self.third_frame, placeholder_text="Enter r",width=600,height=35)
        self.third_entry3.grid(row=5, column=0, padx=20, pady=10)
        
        self.third_entry4 = customtkinter.CTkEntry(self.third_frame, placeholder_text="Enter K",width=600,height=35)
        self.third_entry4.grid(row=6, column=0, padx=20, pady=10)
        
        self.third_frame_button_2 = customtkinter.CTkButton(self.third_frame, text="Calculate", image=self.image_icon_image, compound="right",width=600,height=60,command=self.calculate_event2)
        self.third_frame_button_2.grid(row=7, column=0, padx=20, pady=10)
        
        self.textbox_third_frame = customtkinter.CTkTextbox(self.third_frame,width=300,height=60,)
        self.textbox_third_frame.grid(row=2, column=3,padx=20, pady=10)
        
        self.textbox_third_frame2 = customtkinter.CTkTextbox(self.third_frame,width=300,height=60,)
        self.textbox_third_frame2.grid(row=3, column=3,padx=20, pady=10)

        # create forth frame 
        self.forth_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.forth_frame.grid_columnconfigure(0, weight=1)

        # select default frame
        self.select_frame_by_name("home")
    def upload_excel_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx;*.xls")])
        if file_path:
            self.second_entry1.delete(0, "end")  # Clear any existing text
            self.second_entry1.insert(0, file_path)  # Insert the selected file path

    def calculate_event1(self):
        try:
            # Retrieve values from entry widgets
            path_to_excel = self.second_entry1.get()
            d = float(self.second_entry2.get())
            r = float(self.second_entry3.get())
            k = float(self.second_entry4.get())

            # Read Excel file
            df = pd.read_excel(path_to_excel)

            a = df['α (Lreal)'] = pd.to_numeric(df['α (Lreal)'], errors='coerce')
            L = df["L hooghoudt(cm)"] = pd.to_numeric(df['L hooghoudt(cm)'], errors='coerce')
            H = df["Hdr, сm"] = pd.to_numeric(df['Hdr, сm'], errors='coerce')
            q = df["Drainage,q cm/hr"] = pd.to_numeric(df['Drainage,q cm/hr'], errors='coerce')

            ln = np.log(d/r)
            df['Ln(d/r)']=ln
            lnl = np.log(L/r)
            
            df['dl'] = d / L
            # new_filter = df[df['dl'] < 0.3]
            df['de 0<de<0.3'] = np.where(df['dl'] < 0.3 , d/(1+(d/L)*((8/np.pi)*ln-a)), '')
            df['de 0<de<0.3'] = pd.to_numeric(df['de 0<de<0.3'], errors='coerce')

            df['del de>0.3'] = np.where(df['dl'] > 0.3, (L*np.pi)/8*(lnl-1.15), '')
            df['del de>0.3'] = pd.to_numeric(df['del de>0.3'], errors='coerce')

            
            L_p2 = ((4*k*(H*H))/q) + ((8*k*df['de 0<de<0.3']*H)/q) 
            df['L^2 0<de<0.3']= L_p2

            L_p1 = ((4*k*(H*H))/q) + ((8*k*df['del de>0.3']*H)/q) 
            df['L^2 de>0.3']= L_p1
            geomean1 = np.exp(np.mean(np.log(df['del de>0.3'])))
            last_row = len(df.index) - 1  # index of last row
            df.iloc[last_row, df.columns.get_loc('del de>0.3')] = geomean1

            geomean2 = np.exp(np.mean(np.log(df['de 0<de<0.3'])))
            last_row = len(df.index) - 1  # index of last row
            df.iloc[last_row, df.columns.get_loc('de 0<de<0.3')] = geomean2
            
            # Calculate the averages and geomeans
            de_mean = df['de 0<de<0.3'].mean()
            del_mean = df['del de>0.3'].mean()
            de_geomean = gmean(df['de 0<de<0.3'])
            del_geomean = gmean(df['del de>0.3'])

            # Add the averages and geomeans to the DataFrame
            last_row = len(df.index) - 1
            df.loc[last_row + 1, 'del de>0.3'] = np.nan
            df.loc[last_row + 2, 'de 0<de<0.3'] = np.nan
            df.loc[last_row + 3, 'del de>0.3'] = 'Average'
            df.loc[last_row + 3, 'de 0<de<0.3'] = 'Average'
            df.loc[last_row + 4, 'del de>0.3'] = del_mean
            df.loc[last_row + 4, 'de 0<de<0.3'] = de_mean
            df.loc[last_row + 5, 'del de>0.3'] = 'Geometric Mean'
            df.loc[last_row + 5, 'de 0<de<0.3'] = 'Geometric Mean'
            df.loc[last_row + 6, 'del de>0.3'] = del_geomean
            df.loc[last_row + 6, 'de 0<de<0.3'] = de_geomean

             # Create a new DataFrame with relevant columns for new results
            new_results_df = df[['de 0<de<0.3', 'del de>0.3','L^2 0<de<0.3','L^2 de>0.3']]

            # Save the new DataFrame to a new Excel file
            result_folder = 'results'
            os.makedirs(result_folder, exist_ok=True)
            new_result_file_path = os.path.join(result_folder, 'hooghoudt2022.xlsx')
            new_results_df.to_excel(new_result_file_path, index=False)

            # Print a message or update the UI to indicate the file has been saved
            print(f"New results saved to {new_result_file_path}")
            messagebox.showinfo("Succses", "The File in result/hoogdoudt2022.xlsx")
            # Open the result file
            result_df = pd.read_excel("results/hooghoudt2022.xlsx")

            # Ensure 'de 0<de<0.3' column contains numeric values
            result_df['de 0<de<0.3'] = pd.to_numeric(result_df['de 0<de<0.3'], errors='coerce')
            result_df['del de>0.3'] = pd.to_numeric(result_df['del de>0.3'], errors='coerce')

            # Calculate the arithmetic mean for 'de 0<de<0.3'
            arithmetic_mean_de = result_df['de 0<de<0.3'].mean()
            arithmetic_mean_dee = result_df['del de>0.3'].mean()

            # Display the arithmetic mean in the designated textbox
            self.textbox_second_frame.insert("1.0", f"Y (Констант) (de 0<de<0.3):\n {str(arithmetic_mean_de)}\n")
            self.textbox_second_frame2.insert("1.0", f"Y (Констант) (del de>0.3):\n {str(arithmetic_mean_dee)}\n")


        except Exception as e:
            # Handle exceptions, display an error message, or log the error
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

    def calculate_event2(self):
        try:
             # Read Excel file
            file_path1 = self.third_entry1.get()
            if file_path1:
                df = pd.read_excel(file_path1)

                # Calculate sum of two columns
                # don't forget the pi
                k = df["K, m/d"]= pd.to_numeric(df['K, m/d'], errors='coerce')
                h = df["h=Hdr-m-d, m"]= pd.to_numeric(df['h=Hdr-m-d, m'], errors='coerce')
                q = df["Drainage,q m/d"]= pd.to_numeric(df['Drainage,q m/d'], errors='coerce')
                b = df["Breal, m"]= pd.to_numeric(df['Breal, m'], errors='coerce')
                d = df["d, m"]= pd.to_numeric(df['d, m'], errors='coerce')
                bb = np.log(b/d)-1

                sum_col = (np.pi * k * h)/(q*(bb))

                # Add the sum to a new column
                df['B'] = sum_col
                df["B"]= pd.to_numeric(df['B'], errors='coerce')
                
                df['B/Breal, m']=sum_col/b
                df['B/Breal, m']= pd.to_numeric(df['B/Breal, m'], errors='coerce')

                new_results_df = df[['B/Breal, m']]

                # Save the new DataFrame to a new Excel file
                result_folder = 'results'
                os.makedirs(result_folder, exist_ok=True)
                new_result_file_path = os.path.join(result_folder, 'Костиков(Hdr-m-d).xlsx')
                new_results_df.to_excel(new_result_file_path, index=False)
                messagebox.showinfo("File Processed", "File processed successfully!  By Name Костиков(Hdr-m-d).xlsx")

                # Open the result file
                result_df = pd.read_excel("results/Костиков(Hdr-m-d).xlsx")

                # Ensure 'B/Breal, m' column contains numeric values
                result_df['B/Breal, m'] = pd.to_numeric(result_df['B/Breal, m'], errors='coerce')
                
                self.textbox_third_frame.insert("1.0", f"B/Breal, m:\n {str(result_df['B/Breal, m'])}\n")
        except Exception as e:
            # Handle exceptions, display an error message, or log the error
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

    def calculate_event3(self):
        try:
            path_to_excel = self.third_entry1.get()
        except Exception as e:
            # Handle exceptions, display an error message, or log the error
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

    def select_frame_by_name(self, name):
        # set button color for selected button
        self.home_button.configure(fg_color=("gray75", "gray25") if name == "home" else "transparent")
        self.frame_2_button.configure(fg_color=("gray75", "gray25") if name == "frame_2" else "transparent")
        self.frame_3_button.configure(fg_color=("gray75", "gray25") if name == "frame_3" else "transparent")
        self.frame_4_button.configure(fg_color=("gray75", "gray25") if name == "frame_4" else "transparent")

        # show selected frame
        if name == "home":
            self.home_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.home_frame.grid_forget()
        if name == "frame_2":
            self.second_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.second_frame.grid_forget()
        if name == "frame_3":
            self.third_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.third_frame.grid_forget()
        if name == "frame_4":
            self.forth_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.forth_frame.grid_forget()

    def home_button_event(self):
        self.select_frame_by_name("home")

    def frame_2_button_event(self):
        self.select_frame_by_name("frame_2")

    def frame_3_button_event(self):
        self.select_frame_by_name("frame_3")
    
    def frame_4_button_event(self):
        self.select_frame_by_name("frame_4")

    def change_appearance_mode_event(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)


if __name__ == "__main__":
    app = App()
    app.mainloop()

