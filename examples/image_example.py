import customtkinter
import os
from PIL import Image
import pandas as pd
import numpy as np
from scipy.stats import gmean
from tkinter import filedialog  # Import the file dialog module
from tkinter import messagebox
from scipy.stats import gmean  # Import gmean from scipy.stats
import matplotlib.pyplot as plt


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("image_example.py")
        self.geometry("1000x700")

        # set grid layout 1x2
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # load images with light and dark mode image
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "test_images")
        self.logo_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "CustomTkinter_logo_single.png")),
                                                 size=(26, 26))
        self.large_test_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "about.png")),
                                                       size=(600, 220))
        self.hoogot_test_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "dedede.png")),
                                                        size=(600, 220))
        self.agebt_test_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "Bb.png")), size=(600, 220))
        self.kocho_test_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "bbb.png")), size=(600, 220))
        self.image_icon_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "image_icon_light.png")),
                                                       size=(20, 20))
        self.home_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "home_dark.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "home_light.png")),
                                                 size=(20, 20))
        self.chat_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "chat_dark.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "chat_light.png")),
                                                 size=(20, 20))
        self.add_user_image = customtkinter.CTkImage(
            light_image=Image.open(os.path.join(image_path, "add_user_dark.png")),
            dark_image=Image.open(os.path.join(image_path, "add_user_light.png")), size=(20, 20))

        # create navigation frame
        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(5, weight=1)

        self.navigation_frame_label = customtkinter.CTkLabel(self.navigation_frame, text="  ", image=self.logo_image,
                                                             compound="left",
                                                             font=customtkinter.CTkFont(size=15, weight="bold"))
        self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)

        self.home_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10,
                                                   text="hooghoudt",
                                                   fg_color="transparent", text_color=("gray10", "gray90"),
                                                   hover_color=("gray70", "gray30"),
                                                   image=self.chat_image, anchor="w", command=self.home_button_event)
        self.home_button.grid(row=1, column=0, sticky="ew")

        self.frame_2_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40,
                                                      border_spacing=10, text="Аверьянов",
                                                      fg_color="transparent", text_color=("gray10", "gray90"),
                                                      hover_color=("gray70", "gray30"),
                                                      image=self.add_user_image, anchor="w",
                                                      command=self.frame_2_button_event)
        self.frame_2_button.grid(row=2, column=0, sticky="ew")

        self.frame_4_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40,
                                                      border_spacing=10, text="Костяков",
                                                      fg_color="transparent", text_color=("gray10", "gray90"),
                                                      hover_color=("gray70", "gray30"),
                                                      image=self.add_user_image, anchor="w",
                                                      command=self.frame_4_button_event)
        self.frame_4_button.grid(row=3, column=0, sticky="ew")

        self.frame_3_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40,
                                                      border_spacing=10, text="о нас",
                                                      fg_color="transparent", text_color=("gray10", "gray90"),
                                                      hover_color=("gray70", "gray30"),
                                                      image=self.add_user_image, anchor="w",
                                                      command=self.frame_3_button_event)
        self.frame_3_button.grid(row=4, column=0, sticky="ew")

        self.appearance_mode_menu = customtkinter.CTkOptionMenu(self.navigation_frame,
                                                                values=["Light", "Dark", "System"],
                                                                command=self.change_appearance_mode_event)
        self.appearance_mode_menu.grid(row=6, column=0, padx=20, pady=20, sticky="s")

        # create home hogo
        self.home_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.home_frame.grid_columnconfigure(0, weight=1)

        # create home abetchee
        self.second_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.second_frame.grid_columnconfigure(0, weight=1)

        # create home kochoo
        self.third_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.third_frame.grid_columnconfigure(0, weight=1)

        self.forth_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.forth_frame.grid_columnconfigure(0, weight=1)

        # create home about
        self.third_frame_large_image_label = customtkinter.CTkLabel(self.third_frame, text="",
                                                                    image=self.large_test_image)
        self.third_frame_large_image_label.grid(row=0, column=0, padx=20, pady=10)

        # hogo
        self.second_frame_large_image_label = customtkinter.CTkLabel(self.home_frame, text="",
                                                                     image=self.hoogot_test_image, width=600)
        self.second_frame_large_image_label.grid(row=0, column=0, padx=20, pady=10)

        self.second_frame_button_1 = customtkinter.CTkButton(self.home_frame, text="Upload Excel File",
                                                             image=self.image_icon_image, compound="right", width=600,
                                                             height=60, command=self.upload_excel_file1)
        self.second_frame_button_1.grid(row=2, column=0, padx=20, pady=10)
        self.second_entry1 = customtkinter.CTkEntry(self.home_frame, placeholder_text="Path/To/Excel", width=600,
                                                    height=50)
        self.second_entry1.grid(row=3, column=0, padx=20, pady=10)

        self.second_frame_button_2 = customtkinter.CTkButton(self.home_frame, text="Calculate",
                                                             image=self.image_icon_image, compound="right", width=600,
                                                             height=60, command=self.calculate_event1)
        self.second_frame_button_2.grid(row=4, column=0, padx=20, pady=10)

        self.textbox_second_frame = customtkinter.CTkTextbox(self.home_frame, width=300, height=60, )
        self.textbox_second_frame.grid(row=5, column=0, padx=20, pady=10)

        # abechee
        self.home_frame_large_image_label = customtkinter.CTkLabel(self.second_frame, text="",
                                                                   image=self.agebt_test_image, width=600)
        self.home_frame_large_image_label.grid(row=0, column=0, padx=20, pady=20)

        self.home_frame_button_1 = customtkinter.CTkButton(self.second_frame, text="Upload Excel File",
                                                           image=self.image_icon_image, compound="right", width=600,
                                                           height=60, command=self.upload_excel_file2)
        self.home_frame_button_1.grid(row=2, column=0, padx=20, pady=10)
        self.home_entry1 = customtkinter.CTkEntry(self.second_frame, placeholder_text="Path/To/Excel", width=600,
                                                  height=50)
        self.home_entry1.grid(row=3, column=0, padx=20, pady=10)

        self.home_frame_button_2 = customtkinter.CTkButton(self.second_frame, text="Calculate",
                                                           image=self.image_icon_image, compound="right", width=600,
                                                           height=60, command=self.calculate_event2)
        self.home_frame_button_2.grid(row=4, column=0, padx=20, pady=10)

        self.textbox_home_frame = customtkinter.CTkTextbox(self.second_frame, width=300, height=60, )
        self.textbox_home_frame.grid(row=5, column=0, padx=20, pady=10)

        # kochoo
        self.forth_frame_large_image_label = customtkinter.CTkLabel(self.forth_frame, text="",
                                                                    image=self.kocho_test_image, width=600)
        self.forth_frame_large_image_label.grid(row=0, column=0, padx=20, pady=10)

        self.forth_frame_button_1 = customtkinter.CTkButton(self.forth_frame, text="Upload Excel File",
                                                            image=self.image_icon_image, compound="right", width=600,
                                                            height=60, command=self.upload_excel_file3)
        self.forth_frame_button_1.grid(row=2, column=0, padx=20, pady=10)
        self.forth_entry1 = customtkinter.CTkEntry(self.forth_frame, placeholder_text="Path/To/Excel", width=600,
                                                   height=50)
        self.forth_entry1.grid(row=3, column=0, padx=20, pady=10)

        self.forth_frame_button_2 = customtkinter.CTkButton(self.forth_frame, text="Calculate",
                                                            image=self.image_icon_image, compound="right", width=600,
                                                            height=60, command=self.calculate_event3)
        self.forth_frame_button_2.grid(row=4, column=0, padx=20, pady=10)

        self.textbox_forth_frame = customtkinter.CTkTextbox(self.forth_frame, width=300, height=60, )
        self.textbox_forth_frame.grid(row=5, column=0, padx=20, pady=10)

        # about
        self.textbox_third_frame = customtkinter.CTkTextbox(self.third_frame, width=600, height=300)
        self.textbox_third_frame.grid(row=1, column=0, padx=20, pady=10)
        self.textbox_third_frame.insert("1.0",
                                        "\nНИУ МГСУ \n Хадж Кхамис Рафа, асперантка кафедрой гидравлики и гидротехнического строительства. \n\n\n\n \n Дмитрий Вячеславович Козлов,профессор,\n доктор технических наук,заведующий кафедрой Гидравлики и гидротехнического строительства НИУ МГСУ")
        self.textbox_third_frame.configure(state='disabled')  # Set the state to DISABLED
        # self.third_frame_large_image_label = customtkinter.CTkLabel(self.third_frame, text="", image=self.agebt_test_image,width=600)
        # self.third_frame_large_image_label.grid(row=0, column=0, padx=20, pady=10)

        # self.third_frame_button_1 = customtkinter.CTkButton(self.third_frame, text="Upload Excel File", image=self.image_icon_image, compound="right",width=600,height=60,command=self.upload_excel_file)
        # self.third_frame_button_1.grid(row=2, column=0, padx=20, pady=10)
        # self.third_entry1 = customtkinter.CTkEntry(self.third_frame, placeholder_text="Path/To/Excel",width=600,height=50)
        # self.third_entry1.grid(row=3, column=0, padx=20, pady=10)

        # self.third_entry2 = customtkinter.CTkEntry(self.third_frame, placeholder_text="Enter d",width=600,height=35)
        # self.third_entry2.grid(row=4, column=0, padx=20, pady=10)

        # self.third_entry3 = customtkinter.CTkEntry(self.third_frame, placeholder_text="Enter r",width=600,height=35)
        # self.third_entry3.grid(row=5, column=0, padx=20, pady=10)

        # self.third_entry4 = customtkinter.CTkEntry(self.third_frame, placeholder_text="Enter K",width=600,height=35)
        # self.third_entry4.grid(row=6, column=0, padx=20, pady=10)

        # self.third_frame_button_2 = customtkinter.CTkButton(self.third_frame, text="Calculate", image=self.image_icon_image, compound="right",width=600,height=60,command=self.calculate_event2)
        # self.third_frame_button_2.grid(row=7, column=0, padx=20, pady=10)

        # self.textbox_third_frame = customtkinter.CTkTextbox(self.third_frame,width=300,height=60,)
        # self.textbox_third_frame.grid(row=2, column=3,padx=20, pady=10)

        # self.textbox_third_frame2 = customtkinter.CTkTextbox(self.third_frame,width=300,height=60,)
        # self.textbox_third_frame2.grid(row=3, column=3,padx=20, pady=10)

        # create forth frame

        # select default frame
        self.select_frame_by_name("home")

    def upload_excel_file1(self):
        file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx;*.xls")])
        if file_path:
            self.second_entry1.delete(0, "end")  # Clear any existing text
            self.second_entry1.insert(0, file_path)  # Insert the selected file path

    def upload_excel_file2(self):
        file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx;*.xls")])
        if file_path:
            self.home_entry1.delete(0, "end")  # Clear any existing text
            self.home_entry1.insert(0, file_path)  # Insert the selected file path

    def upload_excel_file3(self):
        file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx;*.xls")])
        if file_path:
            self.forth_entry1.delete(0, "end")  # Clear any existing text
            self.forth_entry1.insert(0, file_path)  # Insert the selected file path

    def calculate_event1(self):
        try:
            # Retrieve values from entry widgets
            path_to_excel = self.second_entry1.get()

            # Read Excel file
            df = pd.read_excel(path_to_excel)
            r = df['r =diameter/2 (cm)'] = pd.to_numeric(df['r =diameter/2 (cm)'], errors='coerce')
            k = df['K, cm/hour'] = pd.to_numeric(df['K, cm/hour'], errors='coerce')
            Lreal = df['L(real) cm'] = pd.to_numeric(df['L(real) cm'], errors='coerce')
            d = df['d hooghoudt, cm'] = pd.to_numeric(df['d hooghoudt, cm'], errors='coerce')
            h = df['∆h=Hdr-w(DMod), cm'] = pd.to_numeric(df['∆h=Hdr-w(DMod), cm'], errors='coerce')
            dr = df['Drainage,q cm/hr'] = pd.to_numeric(df['Drainage,q cm/hr'], errors='coerce')

            df['de (cm) глубкий(L=2500)'] = ((Lreal * np.pi) / (8 * (np.log(Lreal / r) - 1.15)))
            de1 = df['de (cm) глубкий(L=2500)']
            df['α (Lreal)'] = (3.55 - ((1.6 * d) / Lreal) + 2 * ((2 / Lreal) ** 2))
            alfa = df['α (Lreal)'] = pd.to_numeric(df['α (Lreal)'], errors='coerce')
            # df['de (cm) близкий(L=2500)'] = (d/(1+((d/Lreal)*((8/np.pi)*np.log(d/r))-alfa)))
            df['L^2(cm), k=0,4 cm/hour'] = (((4 * 0.4 * h) / dr) * (h + 2 * de1))
            Lsquare = df['L^2(cm), k=0,4 cm/hour']
            df['L hooghoudt(cm)'] = np.sqrt(Lsquare)
            L_hogo = df['L hooghoudt(cm)']
            df['de (cm) близкий(L=2500)s'] = np.where(((d / L_hogo) < 0.3),
                                                      (d / (1 + ((d / Lreal) * ((8 / np.pi) * np.log(d / r)) - alfa))),
                                                      '')
            df['У=L(real) /L hooghoudt'] = Lreal / L_hogo
            Y = df['У=L(real) /L hooghoudt']

            # Save the modified DataFrame back to the same Excel file
            # df.to_excel(path_to_excel, index=False)
            results_folder = "./results/hooghoudt"
            file_name = os.path.basename(path_to_excel)  # Extract the file name from the original path
            result_file_path = os.path.join(results_folder, file_name)

            df.to_excel(result_file_path, index=False)
            # Optionally, you can display a success message
            messagebox.showinfo("Success", "Data saved successfully.")
            # arithmetic_mean_Y = df['У=L(real) /L hooghoudt'].mean()
            arithmetic_mean_Y = df['У=L(real) /L hooghoudt'].mean()
            # arithmetic_gmean_Y = gmean(df['У=L(real) /L hooghoudt'])  # Use gmean from scipy.stats

            # Display the arithmetic mean in the designated textbox
            self.textbox_second_frame.insert("1.0", f"Y (Констант) mean:\n {str(arithmetic_mean_Y)}\n")
            # self.textbox_second_frame2.insert("1.0", f"Y (Констант) geomean:\n {str(arithmetic_gmean_Y)}\n")
            x = df['Date']
            y = df['У=L(real) /L hooghoudt'] = pd.to_numeric(df['У=L(real) /L hooghoudt'],
                                                                       errors='coerce')
            #print(y)
            #print(x)

            # plt.plot(x, y, 'k.', linewidth=2.0)
            # plt.show()

            fig, ax = plt.subplots()
            ax.plot(x, y, linewidth=2.0)
            plt.show()

        except Exception as e:
            # Handle exceptions, display an error message, or log the error
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

    # old
    # a = df['α (Lreal)'] = pd.to_numeric(df['α (Lreal)'], errors='coerce')
    # L = df["L hooghoudt(cm)"] = pd.to_numeric(df['L hooghoudt(cm)'], errors='coerce')
    # H = df["Hdr, сm"] = pd.to_numeric(df['Hdr, сm'], errors='coerce')
    # q = df["Drainage,q cm/hr"] = pd.to_numeric(df['Drainage,q cm/hr'], errors='coerce')

    # ln = np.log(d/r)
    # df['Ln(d/r)']=ln
    # lnl = np.log(L/r)

    # df['dl'] = d / L
    # # new_filter = df[df['dl'] < 0.3]
    # df['de 0<de<0.3'] = np.where(df['dl'] < 0.3 , d/(1+(d/L)*((8/np.pi)*ln-a)), '')
    # df['de 0<de<0.3'] = pd.to_numeric(df['de 0<de<0.3'], errors='coerce')

    # df['del de>0.3'] = np.where(df['dl'] > 0.3, (L*np.pi)/8*(lnl-1.15), '')
    # df['del de>0.3'] = pd.to_numeric(df['del de>0.3'], errors='coerce')

    # L_p2 = ((4*k*(H*H))/q) + ((8*k*df['de 0<de<0.3']*H)/q)
    # df['L^2 0<de<0.3']= L_p2

    # L_p1 = ((4*k*(H*H))/q) + ((8*k*df['del de>0.3']*H)/q)
    # df['L^2 de>0.3']= L_p1
    # geomean1 = np.exp(np.mean(np.log(df['del de>0.3'])))
    # last_row = len(df.index) - 1  # index of last row
    # df.iloc[last_row, df.columns.get_loc('del de>0.3')] = geomean1

    # geomean2 = np.exp(np.mean(np.log(df['de 0<de<0.3'])))
    # last_row = len(df.index) - 1  # index of last row
    # df.iloc[last_row, df.columns.get_loc('de 0<de<0.3')] = geomean2

    # # Calculate the averages and geomeans
    # de_mean = df['de 0<de<0.3'].mean()
    # del_mean = df['del de>0.3'].mean()
    # de_geomean = gmean(df['de 0<de<0.3'])
    # del_geomean = gmean(df['del de>0.3'])

    # # Add the averages and geomeans to the DataFrame
    # last_row = len(df.index) - 1
    # df.loc[last_row + 1, 'del de>0.3'] = np.nan
    # df.loc[last_row + 2, 'de 0<de<0.3'] = np.nan
    # df.loc[last_row + 3, 'del de>0.3'] = 'Average'
    # df.loc[last_row + 3, 'de 0<de<0.3'] = 'Average'
    # df.loc[last_row + 4, 'del de>0.3'] = del_mean
    # df.loc[last_row + 4, 'de 0<de<0.3'] = de_mean
    # df.loc[last_row + 5, 'del de>0.3'] = 'Geometric Mean'
    # df.loc[last_row + 5, 'de 0<de<0.3'] = 'Geometric Mean'
    # df.loc[last_row + 6, 'del de>0.3'] = del_geomean
    # df.loc[last_row + 6, 'de 0<de<0.3'] = de_geomean

    #  # Create a new DataFrame with relevant columns for new results
    # new_results_df = df[['de 0<de<0.3', 'del de>0.3','L^2 0<de<0.3','L^2 de>0.3']]

    # # Save the new DataFrame to a new Excel file
    # result_folder = 'results'
    # os.makedirs(result_folder, exist_ok=True)
    # new_result_file_path = os.path.join(result_folder, 'hooghoudt2022.xlsx')
    # new_results_df.to_excel(new_result_file_path, index=False)

    # # Print a message or update the UI to indicate the file has been saved
    # print(f"New results saved to {new_result_file_path}")
    # messagebox.showinfo("Succses", "The File in result/hoogdoudt2022.xlsx")
    # # Open the result file
    # result_df = pd.read_excel("results/hooghoudt2022.xlsx")

    # # Ensure 'de 0<de<0.3' column contains numeric values
    # result_df['de 0<de<0.3'] = pd.to_numeric(result_df['de 0<de<0.3'], errors='coerce')
    # result_df['del de>0.3'] = pd.to_numeric(result_df['del de>0.3'], errors='coerce')

    # # Calculate the arithmetic mean for 'de 0<de<0.3'
    # arithmetic_mean_de = result_df['de 0<de<0.3'].mean()
    # arithmetic_mean_dee = result_df['del de>0.3'].mean()

    # # Display the arithmetic mean in the designated textbox
    # self.textbox_second_frame.insert("1.0", f"Y (Констант) (de 0<de<0.3):\n {str(arithmetic_mean_de)}\n")
    # self.textbox_second_frame2.insert("1.0", f"Y (Констант) (del de>0.3):\n {str(arithmetic_mean_dee)}\n")

    def calculate_event2(self):
        try:
            # Retrieve values from entry widgets
            path_to_excel = self.home_entry1.get()

            # Read Excel file
            df = pd.read_excel(path_to_excel)
            breal = df['Breal,m'] = pd.to_numeric(df['Breal,m'], errors='coerce')
            T = df['T,m'] = pd.to_numeric(df['T,m'], errors='coerce')
            dp = df['dp=s,m'] = pd.to_numeric(df['dp=s,m'], errors='coerce')
            d = df['dф=dАверя,m'] = pd.to_numeric(df['dф=dАверя,m'], errors='coerce')
            k = df['K,m/d'] = pd.to_numeric(df['K,m/d'], errors='coerce')
            qc = df['qc,m/d'] = pd.to_numeric(df['qc,m/d'], errors='coerce')
            drainage = df['Drainage,q m/d'] = pd.to_numeric(df['Drainage,q m/d'], errors='coerce')
            h = df['h=Hdr-m-d,m'] = pd.to_numeric(df['h=Hdr-m-d,m'], errors='coerce')
            daltah = df['∆h=Hdr-w(DMod)'] = pd.to_numeric(df['∆h=Hdr-w(DMod)'], errors='coerce')

            df['α (Breal)'] = (breal / (breal - ((8 * T) / np.pi) * np.log(np.sin(np.pi * dp) / T)))
            #()
            alfaa = df['α (Breal)']
            # df['B Аверя(уст)'] = (2 * h) * ((k / qc) * (1 + ((2 * T) / h) * alfaa) ** (1 / 2))
            # df['B (α),m'] = df['B Аверя(уст)']
            # df['B (α),m'] = breal / df['B Аверя(уст)']
            # df['B Аверя(неуст)']=((8*k*T*h*alfaa)/(qc)**(1/2))
            # df['Y(неуст)=']=breal/df['B Аверя(неуст)']

            # df['α (Breal)'] = 25
            df['s'] = 0
            s = df['s']

            # iterations = 25
            for num in s:
                if num != 25:
                    s = df['B Аверя(уст)'] = (2 * daltah) * ((k / qc) * (1 + ((2 * T) / daltah) * df['α (Breal)']) ** (1 / 2))
                    num = s

            df['B Аверя(уст)'] = s
            # df['B (α),m'] = df['B Аверя(уст)']
            df['Y= В Аверя / B real'] = df['B Аверя(уст)'] / breal  
            
            results_folder = "./results/Аверьянов"
            file_name = os.path.basename(path_to_excel)  # Extract the file name from the original path
            result_file_path = os.path.join(results_folder, file_name)
            df.to_excel(result_file_path, index=False)
            arithmetic_mean_Y = df['Y= В Аверя / B real'].mean()
            # arithmetic_gmean_Y = gmean(df['У=L(real) /L hooghoudt'])  # Use gmean from scipy.stats

            # Display the arithmetic mean in the designated textbox
            self.textbox_home_frame.insert("1.0", f"Y= В Аверя / B real mean:\n {str(arithmetic_mean_Y)}\n")
            
            messagebox.showinfo("Success", "Data saved successfully.")

            x = df['Date']
            y = df['Y= В Аверя / B real'] = pd.to_numeric(df['Y= В Аверя / B real'],errors='coerce')
            #print(y)
            #print(x)

            # plt.plot(x, y, 'k.', linewidth=2.0)
            # plt.show()

            fig, ax = plt.subplots()
            ax.plot(x, y, linewidth=2.0)
            plt.show()
            # df.to_excel(result_file_path, index=False)
            # Optionally, you can display a success message
            # arithmetic_mean_Y = df['Y(неуст)='].mean()
            # messagebox.showinfo("Success", "Data saved successfully.")
            # self.textbox_home_frame.insert("1.0", f"Y(неуст)=:\n {str(arithmetic_mean_Y)}\n")

            # arithmetic_mean_Y = df['L hooghoudt / У=L(real)'].mean()
            # arithmetic_mean_Y = df['L hooghoudt / У=L(real)'].mean()
            # arithmetic_gmean_Y = gmean(df['У=L(real) /L hooghoudt'])  # Use gmean from scipy.stats

            # Display the arithmetic mean in the designated textbox
            # self.textbox_second_frame.insert("1.0", f"Y (Констант) mean:\n {str(arithmetic_mean_Y)}\n")
            # self.textbox_second_frame2.insert("1.0", f"Y (Констант) geomean:\n {str(arithmetic_gmean_Y)}\n")
        except Exception as e:
            # Handle exceptions, display an error message, or log the error
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

    def calculate_event3(self):
        try:
            # Retrieve values from entry widgets
            path_to_excel = self.forth_entry1.get()

            # Read Excel file
            df = pd.read_excel(path_to_excel)
            # C
            # htot = df['Htot, m'] = pd.to_numeric(df['Htot, m'], errors='coerce')
            # D
            hdr = df['Hdr, m'] = pd.to_numeric(df['Hdr, m'], errors='coerce')
            # E
            # mm = df['m, m'] = pd.to_numeric(df['m, m'], errors='coerce')
            # F
            dm = df['d, m'] = pd.to_numeric(df['d, m'], errors='coerce')
            # G
            # wdmod = df['w(Dmod),cm'] = pd.to_numeric(df['w(Dmod),cm'], errors='coerce')
            # H
            wtd_m = df['Water Table Depth, m'] = pd.to_numeric(df['Water Table Depth, m'], errors='coerce')
            # I
            # daltaH = df['∆h=Hdr-w(DMod), m'] = pd.to_numeric(df['∆h=Hdr-w(DMod), m'], errors='coerce')
            # J
            # h = df['h=Hdr-m-d, m'] = pd.to_numeric(df['h=Hdr-m-d, m'], errors='coerce')
            # K
            # pm = df['Р, m'] = pd.to_numeric(df['Р, m'], errors='coerce')
            # L
            # dring = df['Drainage, cm/d'] = pd.to_numeric(df['Drainage, cm/d'], errors='coerce')
            # M
            dringq = df['Drainage,q m/d'] = pd.to_numeric(df['Drainage,q m/d'], errors='coerce')
            # N
            # qc = df['qc,m/d'] = pd.to_numeric(df['qc,m/d'], errors='coerce')
            # O
            k = df['K, m/d'] = pd.to_numeric(df['K, m/d'], errors='coerce')
            # P
            breal = df['Breal, m'] = pd.to_numeric(df['Breal, m'], errors='coerce')

            df['∆h=Hdr-w(DMod), m'] = hdr - wtd_m
            daltaH = df['∆h=Hdr-w(DMod), m']
            df['h=Hdr-m-d, m'] = hdr - 0.75 - dm
            h = df['h=Hdr-m-d, m']

            # bbbb = df['B костяков, m']=(np.pi*k*daltaH)/(dringq*(np.log(bbbb/dm)-1))
            df['B костяков, m'] = 25
            df['s'] = 0
            s = df['s']

            # iterations = 25
            for num in s:
                if num != 25:
                    s = df['B костяков, m'] = (np.pi * k * daltaH) / (dringq * (np.log(df['B костяков, m'] / dm) - 1))
                    num = s

            df['B костяков, m'] = s
            df['B костяков/B real'] = (df['B костяков, m'] / breal)
            df['B костяков для проекта, m'] = (np.pi * k * h) / (dringq * (np.log(df['B костяков, m'] / dm) - 1))
            df['B костяков для проекта, m/B real'] = (df['B костяков для проекта, m'] / breal)

            results_folder = "./results/Костиков"
            file_name = os.path.basename(path_to_excel)  # Extract the file name from the original path
            result_file_path = os.path.join(results_folder, file_name)

            df.to_excel(result_file_path, index=False)
            # Optionally, you can display a success message
            arithmetic_mean_Y = df['B костяков/B real'].mean()
            messagebox.showinfo("Success", "Data saved successfully.")
            self.textbox_forth_frame.insert("1.0", f"B костяков/B real=:\n {str(arithmetic_mean_Y)}\n")

            x = df['Date']
            y = df['B костяков для проекта, m/B real'] = pd.to_numeric(df['B костяков для проекта, m/B real'],
                                                                       errors='coerce')
            #print(y)
            #print(x)

            # plt.plot(x, y, 'k.', linewidth=2.0)
            # plt.show()

            fig, ax = plt.subplots()
            ax.plot(x, y, linewidth=2.0)
            plt.show()

            # arithmetic_mean_Y = df['L hooghoudt / У=L(real)'].mean()
            # arithmetic_mean_Y = df['L hooghoudt / У=L(real)'].mean()
            # # arithmetic_gmean_Y = gmean(df['У=L(real) /L hooghoudt'])  # Use gmean from scipy.stats

            # # Display the arithmetic mean in the designated textbox
            # self.textbox_second_frame.insert("1.0", f"Y (Констант) mean:\n {str(arithmetic_mean_Y)}\n")
            # # self.textbox_second_frame2.insert("1.0", f"Y (Констант) geomean:\n {str(arithmetic_gmean_Y)}\n")
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
