import matplotlib
from matplotlib import style
from tkinter import filedialog
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rc,rcParams
from pylab import *


import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter.ttk import *
from time import strftime 


LARGE_FONT= ("Helvetica", 18)
style.use("ggplot")
SMALL_FONT= ('Helvetica',10,'bold')
SMALL_FONT_=('Helvetica',12,'bold')

'''
f = Figure(figsize=(5,5), dpi=100)
a = f.add_subplot(111)
'''

#TAKEOFF #HOVER LAND OFF

def quit():
    quit()
'''
def animate(i):
    pullData = pd.read_csv('sampleText.csv')
    xList = pullData.iloc[:,1]
    yList = pullData.iloc[:,2]

    a.plot(xList,'r',label=xx)
    a.plot(yList,'g',label=yy)
    a.legend(loc="upper right")
'''


class iFapp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        tk.Tk.iconbitmap(self, default="ideaforge.ico")
        tk.Tk.wm_title(self, "Log File Analysis System")
        
        my_menu = Menu(self)
        param_menu = Menu(self, tearoff = False)
        phi_menu = Menu(self, tearoff = False)
        the_menu = Menu(self, tearoff = False)
        psi_menu = Menu(self, tearoff = False)
        cont_psi_menu = Menu(self, tearoff = False)
        alt_menu = Menu(self, tearoff = False)
        throttle_menu = Menu(self, tearoff = False)
        voltage_menu = Menu(self, tearoff = False)
        gps_sat_menu = Menu(self, tearoff = False)
        gps_hdop_menu = Menu(self, tearoff = False)
        motor_menu = Menu(self, tearoff = False)
        mag_menu = Menu(self, tearoff = False)
        iaz_menu = Menu(self, tearoff = False)

        #param_menu = Menu(param_menu, tearoff = False)

        self.config(menu = my_menu)
        
        global phi_min, phi_max, phi_overlapp, the_max, the_min, the_overlapp, psi_max, psi_min, psi_overlapp, cont_psi_average,alt_overlapp, throttle_max, voltage_max, gps_min, gps_hdop_max, motor_overlapp, mag_min, mag_max, iaz_max

        phi_min = -16
        phi_max = 16
        phi_overlapp = 5
        the_min = -16
        the_max = 16
        the_overlapp = 5
        psi_min = -100
        psi_max = 100
        psi_overlapp = 5
        cont_psi_average = 100
        alt_overlapp = 10
        throttle_max = 90
        voltage_max = 10
        gps_min = 10
        gps_hdop_max = 1 
        motor_overlapp = 10
        mag_min = 60
        mag_max = 100
        iaz_max = 5

        def phi_min_txt():
            global phi_min
            phi_min = simpledialog.askfloat("min value", "set value" )
           
        def the_min_txt():
            global the_min
            the_min = simpledialog.askfloat("min value", "set value" )
            
        def psi_min_txt():
            global psi_min
            psi_min = simpledialog.askfloat("min value", "set value" )
            
        def phi_max_txt():
            global phi_max
            phi_max = simpledialog.askfloat("max value", " set value")

        def the_max_txt():
            global the_max
            the_max = simpledialog.askfloat("max value", " set value")

        def psi_max_txt():
            global psi_max
            psi_max = simpledialog.askfloat("max value", " set value")
            

        def phi_overlapp_txt():
            global phi_overlapp
            phi_overlapp = simpledialog.askfloat("overlapp parameter", "set value")
            

        def the_overlapp_txt():
            global the_overlapp
            the_overlapp = simpledialog.askfloat("overlapp parameter", "set value")
            

        def psi_overlapp_txt():
            global psi_overlapp
            psi_overlapp = simpledialog.askfloat("overlapp parameter", "set value")
            

        def cont_psi_average_txt():
            global cont_psi_average
            cont_psi_average = simpledialog.askfloat("Controller Psi average value", " set value")

        def alt_overlapp_txt():
            global alt_overlapp
            alt_overlapp = simpledialog.askfloat("overlapp parameter", "set value")

        def throttle_max_txt():
            global throttle_max
            throttle_max = simpledialog.askfloat("max value", " set value")
            

        def voltage_max_txt():
            global voltage_max
            voltage_max = simpledialog.askfloat("max value", " set value")


        def gps_min_txt():
            global gps_min
            gps_min = simpledialog.askfloat("min value", " set value")

        def gps_hdop_max_txt():
            global gps_hdop_max
            gps_hdop_max = simpledialog.askfloat("max value", " set value")

        def motor_overlapp_txt():
            global motor_overalapp
            motor_overalapp = simpledialog.askfloat("overlapp parameter", "set value")

        def mag_min_txt():
            global mag_min
            mag_min = simpledialog.askfloat("min value", " set value")

        def mag_max_txt():
            global mag_max
            mag_max = simpledialog.askfloat("max value", " set value")

        def iaz_max_txt():
            global iaz_max
            iaz_max = simpledialog.askfloat("max value", " set value")

        def password_input():
            user_input = simpledialog.askstring("Enter Password", "Password" , show = '*')
            if user_input != " ":
                messagebox.showinfo("Exit", "Wrong Password") 
            if user_input == " ":
                file_menu.add_cascade(label = " Set Parameters ", menu = param_menu)
                param_menu.add_cascade(label = " Phi and Desired Phi ", menu = phi_menu)
                phi_menu.add_command(label = "Min value", command = lambda:phi_min_txt())
                phi_menu.add_command(label = "Max value", command = lambda:phi_max_txt())
                phi_menu.add_command(label = "Overlapp parameter", command = lambda:phi_overlapp_txt())

                param_menu.add_cascade(label = " The and Desired The ", menu = the_menu)
                the_menu.add_command(label = "Min value", command = lambda:the_min_txt())
                the_menu.add_command(label = "Max value", command = lambda:the_max_txt())
                the_menu.add_command(label = "Overlapp parameter", command = lambda:the_overlapp_txt())
                
                param_menu.add_cascade(label = " Psi and Desired Psi ", menu = psi_menu)
                psi_menu.add_command(label = "Min value", command = lambda:psi_min_txt())
                psi_menu.add_command(label = "Max value", command = lambda:psi_max_txt())
                psi_menu.add_command(label = "Overlapp parameter", command = lambda:psi_overlapp_txt())
                
                param_menu.add_cascade(label = " Controller Psi and Psi ", menu = cont_psi_menu)
                cont_psi_menu.add_command(label = " Max Average Value ", command = lambda:cont_psi_average_txt())

                param_menu.add_cascade(label = " Altitude and desired altitude ", menu = alt_menu)
                alt_menu.add_command(label = " Overlapp parameter", command = lambda:alt_overlapp_txt())

                param_menu.add_cascade(label = " Max Throttle ", menu = throttle_menu)
                throttle_menu.add_command(label = " Max throttle ", command = lambda:throttle_max_txt())

                param_menu.add_cascade(label = " Voltage and mid-voltage ", menu = voltage_menu)
                voltage_menu.add_command(label = " Spike parameter ", command = lambda:voltage_max_txt())

                param_menu.add_cascade(label = " GPS A & B value ", menu = gps_sat_menu)
                gps_sat_menu.add_command(label = " GPS sat value ", command = lambda:gps_min_txt())

                param_menu.add_cascade(label = " GPS A & B HDOP ", menu =gps_hdop_menu)
                gps_hdop_menu.add_command(label = " GPS hdop value ", command = lambda:gps_hdop_max_txt())

                param_menu.add_cascade(label = " Motor PWM ", menu = motor_menu)
                motor_menu.add_command(label = " PWM overlapp ", command = lambda:motor_overlapp_txt())

                param_menu.add_cascade(label = " Mag Field ", menu = mag_menu)
                mag_menu.add_command(label = " Min mag_field ", command = lambda:mag_min_txt())
                mag_menu.add_command(label = " Max mag_field", command = lambda:mag_max_txt())
                
                param_menu.add_cascade(label = " I Az vibration ", menu = iaz_menu)
                iaz_menu.add_command(label = " Max I Az vibration value ", command = lambda:iaz_max_txt())

        file_menu = Menu(my_menu, tearoff = False)
        my_menu.add_cascade(label = " Admin Settings", menu = file_menu)
        file_menu.add_command(label="Enter Password", command = password_input)
        
        container = tk.Frame(self)
        container.pack()
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, PageOne, PageTwo, PageThree):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

        def get_page(self, page_class):
            return self.frames[page_class]
        
    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

 
class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller=controller
        canvas1 = tk.Canvas(self, width = 650, height = 520, bg = 'black', relief = 'raised')
        canvas1.pack(side ="top",fill="both",expand="True")

        style=Style()

        style.configure('l.TButton', font =
               ('Helvetica', 26, 'bold'),
                foreground = 'black',background= 'black')

        label = ttk.Label(self, text="Log File Visualizer",style='l.TButton',width=17)
        #label.pack(pady=10,padx=10)
        canvas1.create_window(326,27, window = label)

    
        #button.pack()
        

        button2 = ttk.Button(self, text="Log CheckList",
                            command=lambda: my_command2())
        canvas1.create_window(500,470, window = button2)
        #button2.pack()
        
        style=Style()

        style.configure('y.TButton', font =
               ('calibri', 10, 'bold', 'underline'),
                foreground = 'green',background='black') 
        
        button3 = ttk.Button(self, text="Plot Graph", style='y.TButton',
                            command=lambda: my_command1())
        canvas1.create_window(320,300, window = button3)

        style=Style()

        style.configure('c.TButton', font =
               ('calibri', 10,),
                foreground = 'black',background='black') 

        button = ttk.Button(self, text="Comm Check Page", style='c.TButton',
                            command=lambda: controller.show_frame(PageOne))
        canvas1.create_window(150,470, window = button)

        #button3.pack()
        
        global var, flight_status
        var=dict()

        flight_status=['OFF','STARTUP','TAKEOFF','HOVER','LAND']
        
        def my_command1():
            data = pd.DataFrame(df,columns = [my_combo.get(),my_combo1.get(),'Mode', 'Wind'])
            #print(type(z))
            temp = " "
            for i in flight_status:
                data.replace(to_replace = i, value = var[i].get(), inplace = True)
                if (var[i].get() == 1):
                    temp+=" "+i
            x=str(uav_label).replace('(','').replace(')','').replace('(','').replace(')','').replace(',','').replace(',','')
            temp="UAV ID:"+" "+x+"  "+"Mode:"+""+temp
            
            option=['1']
            new_data=data.loc[data['Mode'].isin(option)]

            #new_z=z.loc[z['Mode'].isin(options)]
            
            new_data.to_csv('sampleText.csv')

            #print((new_z))
            
            #new_data.to_csv('sampleText.csv')

            global my_string
            if (lat_long_var.get() == 1):
                my_string = "Lat: "+ str(lat_data) +"    "+ " Lon: "+ str(long_data)+"    " +" "+"Max-Wind: "+ str(wind_data)
            if (lat_long_var.get() != 1):
                my_string = "Max-Wind: "+ str(wind_data)

            pullData = pd.read_csv('sampleText.csv')
            #print(pullData)
            xList = pullData.iloc[:,1]
            yList = pullData.iloc[:,2]
            zList = pullData.iloc[:,4]
            if (my_combo.get()==my_combo1.get()):
                plt.plot(yList,'g',label = my_combo.get())
                if (wind_chk_var.get() == 1):
                    plt.plot(zList,'b', label = 'wind')
                plt.title(temp)
            else:
                plt.plot(xList,'r',label=my_combo.get())
                plt.plot(yList,'g',label=my_combo1.get())
                if (wind_chk_var.get() == 1):
                    plt.plot(zList,'b', label = 'wind')
                plt.title(temp)
            fig = plt.gcf()
            fig.canvas.set_window_title('Log File Visualizer')
            plt.ylabel(date +"    " +"Flight Num: "+f_num)
            plt.xlabel(my_string)
            plt.legend(loc='upper left')
            plt.show()
            del xList,yList

        
        style=Style()

        style.configure('x.TButton', font =
               ('calibri', 10, 'bold', 'underline'),
                foreground = 'green',background= 'black') 
        browseButton_CSV = ttk.Button(self,text=" Select CSV File ", style='x.TButton',command=lambda:get_CSV())
        canvas1.create_window(320,210, window = browseButton_CSV)

        style=Style()

        style.configure('z.TButton', font =
               ('calibri', 11, 'bold'),
                foreground = 'Black',background= 'green')

        label2 = ttk.Label(self, text="Select Property 1", style='z.TButton')
        canvas1.create_window(150,170, window = label2)

        label3 = ttk.Label(self, text="Select Property 2", style='z.TButton')
        canvas1.create_window(500,170, window = label3)

        style=Style()

        style.configure('u.TButton', font =
               ('calibri', 10, 'bold'),
                foreground = 'green',background= 'black')

        
        global fault,basic_fault_col_names

        basic_fault_col_names=['Phi','Desired Phi','The','Desired The','Psi','Desired Psi','Controller Psi','Psi','Altitude','Desired Altitude','Throttle','Voltage','Mid Voltage','G1 Sat','G1 HDOP','G2 Sat','G2 HDOP','MAG Field','I Az','Mode']


        def get_CSV():
            global df,uav_label
            import numpy as np
            import_file_path = filedialog.askopenfilename()
            df = pd.read_csv (import_file_path)
            # data_col_names=data_col_names.values.tolist()
            global date 
            date = import_file_path
            date = str(date)
            # Extracting date info from the file_name 

            date_list = []
            index = 0 
            count_space = 0 
            index_space = 0

            for i in range(len(date)):
                if date[i] == '/':
                    index = i
                if date[i] == ' ':
                    count_space += 1
                    if count_space == 3:
                        index_space = i
    
            for i in range(index+1,index_space):
                date_list.append(date[i])

            date = " ".join(date_list)
            
            #Flight date information extracted 

            label5 = tk.Label(self, text=import_file_path , bg='lightblue', fg='black', font=SMALL_FONT)
            canvas1.create_window(320,240, window = label5)

            global lat_data,long_data,wind_data, flight_number


            flight_number=np.array(pd.DataFrame(df,columns=['Flight Number']).values.tolist())
            f_status=np.array(pd.DataFrame(df,columns=['Mode']).values.tolist())
            long_data = np.array(pd.DataFrame(df, columns = ['CBX Lon']).values.tolist())
            lat_data = np.array(pd.DataFrame(df, columns = ['CBX Lat']).values.tolist())
            wind_data = np.array(pd.DataFrame(df, columns = ['Wind']).values.tolist())


            long_data = np.average(long_data).round(2)
            lat_data = np.average(lat_data).round(2)
            wind_data = np.max(wind_data).round(2)

            flight_number = np.unique(flight_number)

            global f_num

            f_num = []

            for i in range(len(flight_number)):
                if (flight_number[i] != 0):
                    f_num.append(flight_number[i])

            f_num = str(f_num)
            print(f_num)

            count = 0
            for i in range(len(f_status)):
                if (f_status[i] == 'FS_BATT'):
                    count += 1
                    my_item = 'FS_BATT'
                    if (count > 0):
                        if my_item not in flight_status:
                            flight_status.append('FS_BATT')
                    if (count == 0):
                        if my_item in flight_status:
                            flight_status.remove('FS_BATT')
                            break

            #Check Button for Wind, Latitude-Longitude

            global wind_chk_var
            wind_chk_var = IntVar()
            wind_chk = tk.Checkbutton(self,text = 'Wind Data on plot', variable = wind_chk_var, width = 15, height = 1)
            wind_chk.select()
            canvas1.create_window(500,300, window = wind_chk)

            global lat_long_var
            lat_long_var = IntVar()
            lat_long_chk = tk.Checkbutton(self, text = 'Lat Long Value', variable = lat_long_var, width = 15, height = 1)
            lat_long_chk.select()
            canvas1.create_window(500,320,window = lat_long_chk)


            d=300                      #for positioning of checkboxes
            for i in flight_status:
                var[i]=IntVar()
                chk=tk.Checkbutton(self,text = i,variable = var[i],width = 8, height = 1)
                chk.select()
                canvas1.create_window(150,d,window=chk)
                d+=20

            label4 = ttk.Label(self, text="FLIGHT MODE",style='u.TButton',width=11)
            canvas1.create_window(150,275, window = label4)

            
            data = pd.DataFrame(df,columns = [my_combo.get(),my_combo1.get(),'Mode'])
            data.to_csv('sampleText.csv')
            uav_id=pd.DataFrame(df,columns=['UAV ID']).head(1)
            uav_id=uav_id.values.tolist()
            id1=uav_id
            style=Style()
            style.configure('b.TButton', font =
                ('calibri', 13, 'bold'),
                foreground = 'red',background= 'black')
            UAV= ttk.Label(self, text=uav_id,style='b.TButton',width=11)
            canvas1.create_window(320,100, window = UAV)
            UAV_ID= ttk.Label(self, text="UAV ID",style='b.TButton',width=8)
            canvas1.create_window(320,70, window = UAV_ID)
            uav_label=UAV['text']


        def combo_click(event):
            my_label=tk.Label(self,text=my_combo.get(),bg='black', fg='darkblue', font=LARGE_FONT)
            canvas1.create_window(100,300,window=my_label)

        options =['Phi', 'The', 'Psi', 'Desired Phi', 'Desired The', 'Desired Psi', 'p', 'q', 'r', 'Desired p', 'Desired q', 'Desired r', 'Controller Phi', 'Controller The', 'Controller Psi', 'Controller Phi LPF', 'Controller The LPF', 'Controller Psi LPF', 'Altitude', 'Desired Altitude', 'Track Altitude', 'Safety Altitude', 'Throttle', 'Throttle FW', 'Flaps', 'GPS Lon', 'GPS Lat', 'GPS MSL', 'GPS AGL', 'GPS Speed', 'GPS Head', 'GPS Sat', 'GPS HDOP', 'GPS Date', ' GPS Time', 'Waypoint Lon', 'Waypoint Lat', 'Track Lon', 'Track Lat', 'Home Lon', 'Home Lat', 'Distance to Waypoint', 'Distance to Home', 'Flight Time', 'Mode', 'ASD', 'Wind', 'WindDir', 'Altitude Correction', 'Throttle Adjust', 'Voltage', 'Mid-Voltage', 'Imbalance', 'uC Voltage', 'Sensor Voltage', 'Current', 'CBX Voltage', 'CBX Lon', 'CBX Lat', 'CBX MSL GPS', 'CBX Sat', 'CBX HDOP', 'CBX MSL Pressure', 'CBX Status', 'UAV Status', 'UAV ID', 'Status', 'EXTRA Status', 'RC/sec', 'GS/sec', 'RX/sec', 'Bytes/sec', 'PWM1', 'PWM2', 'PWM3', 'PWM4', 'PWM5', 'PWM6', 'PWM7', 'PWM8', 'PWM9', 'PWM10', 'PWM1 LPF', 'PWM2 LPF', 'PWM3 LPF', 'PWM4 LPF', 'PWM5 LPF', 'PWM6 LPF', 'PWM7 LPF', 'PWM8 LPF', 'PWM9 LPF', 'PWM10 LPF', 'JoyLx', 'JoyLy', 'JoyRx', 'JoyRy', 'Buttons', 'RC1', 'RC2', 'RC3', 'RC4', 'RC5', 'RC6', 'Gp', 'Gq', 'Gr', 'Ax', 'Ay', 'Az', 'Bx', 'By', 'Bz', 'Tx', 'MSL1', 'MSL2', 'MSL3', 'AGL1', 'AGL2', 'AGL3', 'T1', 'T2', 'T3', 'Radar F', 'Radar R', 'Radar B', 'Radar L', 'Sensor Health', 'Sensor Health History', 'G1 Lon', 'G1 Lat', 'G1 MSL', 'G1 AGL', 'G1 Speed', 'G1 Head', 'G1 Sat', 'G1 HDOP', 'G2 Lon', 'G2 Lat', 'G2 MSL', 'G2 AGL', 'G2 Speed', 'G2 Head', 'G2 Sat', 'G2 HDOP', 'I X', 'I XRef', 'I Vx', 'I VxRef', 'I Ax', 'I AxBias', 'I Y', 'I YRef', 'I Vy', 'I VyRef', 'I Ay', 'I AyBias', 'I Z', 'I ZRef', 'I Vz', 'I VzRef', 'I Az', 'I AzBias', 'I Acc Scl', 'MAG Field', 'MAG Error', 'NaN Error', 'uC Percent', 'RTK Fix', 'RTK Heading', 'GCS Battery', 'GCS Storage', 'Flight Number', 'Firmware Version']
        clicked =StringVar()
        clicked.set(options[0])

        my_combo=ttk.Combobox(self,value=options)
        my_combo.current(0)
        my_combo.bind("<<Comboboxselected>>", combo_click)
        canvas1.create_window(150,195,window=my_combo)

        my_combo1=ttk.Combobox(self,value=options)
        my_combo1.current(0)
        my_combo1.bind("<<Comboboxselected>>", combo_click)
        
        
        canvas1.create_window(500,195,window=my_combo1)


        def my_command2():
            '''
            z1=df
            for i in flight_status:
                z1.replace(to_replace = i, value = var[i].get(), inplace = True)
                print(var[i].get())
            option=['1']
            n_z = z1.loc[z1['Mode'].isin(option)]
            '''
            df.to_csv('new_text.csv')
            controller.show_frame(PageTwo)

        #my_button=ttk.Button(self, text='select from the list', command=combo_click)
        #canvas1.create_window(100,550, window=my_button)

class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller=controller
        canvas2 = tk.Canvas(self, width = 650, height = 520, bg = 'black', relief = 'raised')
        canvas2.pack(side ="top",fill="both",expand="True")

        style=Style()

        style.configure('p.TButton', font =
               ('Helvetica', 20, 'bold'),
                foreground = 'red',background= 'red')
        
        label = ttk.Label(self, text='Comm Error msg', style='p.TButton')
        canvas2.create_window(325,25, window=label)

        style=Style()

        style.configure('r.TButton', font =
               ('Helvetica', 10, 'bold'),
                foreground = 'red',background= 'black')

        style.configure('g.TButton', font =
               ('Helvetica', 10, 'bold'),
                foreground = 'green',background= 'black')

        style.configure('bb.TButton', font =
               ('Helvetica', 10, 'bold'),
                foreground = 'black',background= 'blue')

        def comm_command():
            data=df
            import numpy as np
            '''
            def clean_flight_time(x):
                for i in range(len(x)):
                    if isinstance(x[i], str):
                        return(x[i].replace('m', '').replace('s', ''))
                return(x)
            '''
            #data['Flight Time'] = data['Flight Time'].replace({'m':'', 's':''}, regex=True)
            uav_status=np.array(pd.DataFrame(data,columns=['UAV Status']).values.tolist())
            flight_time=(pd.DataFrame(data,columns=['Flight Time']).values.tolist())

            global cont
            cont=[]

            #print(type(flight_time))

            for i in range(len(uav_status)-1):
                if (uav_status[i] != 'UAV / NOT CONNECTED'):
                    if (uav_status[i+1] == 'UAV / NOT CONNECTED'):
                        if (flight_time[i] != ['0m 00s']):
                            cont.append(flight_time[i+1])


                if (uav_status[i] == 'UAV / NOT CONNECTED'):
                    if (uav_status[i+1] != 'UAV / NOT CONNECTED'):
                        if (flight_time[i] != ['0m 00s']):
                            cont.append(flight_time[i])

            
            cont=np.array(cont)

            print(cont)

            global d

            d=150

            global label_dict

            label_dict=['label1','label2','label3','label4','label5','label6','label7','label8']


            if (len(cont) == 0):
                label_dict[0] = tk.Label(self, text=' No COMM FAIL detected ', bg='black',fg='white',width=20, font=SMALL_FONT)
                canvas2.create_window(200,d, window=label_dict[0])

            
            var_dict=dict()

            import math
            #print(label_dict[2])

            for i in range(math.floor(len(cont)/2)):
                txt=str(i+1)+' COMM FAIL at '+str(cont[2*i])+ ' to ' + str(cont[2*(i+1)-1])
                label_dict[i] = tk.Label(self, text=txt, bg='black',fg='white',width=100, font=SMALL_FONT)
                canvas2.create_window(200,d, window=label_dict[i])
                d+=20


        button1 = ttk.Button(self, text=" Comm Check ",style='bb.TButton',
                            command=lambda: comm_command())
        canvas2.create_window(325,60,window=button1)


        import math
        def back_start():
            controller.show_frame(StartPage)
            for i in range(math.floor(len(cont)/2)):
                label_dict[i].destroy()

        style=Style()

        style.configure('u.TButton', font =
               ('calibri', 10, 'bold'),
                foreground = 'green',background= 'black')
        button1 = ttk.Button(self, text="Back to Home",style='r.TButton',
                            command=lambda: back_start())
        canvas2.create_window(565,480,window=button1)

        button2 = ttk.Button(self, text="Log CheckList", style='g.TButton',
                            command=lambda: controller.show_frame(PageTwo))
        canvas2.create_window(325,480,window = button2)


class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller=controller
        
        canvas3 = tk.Canvas(self, width = 650, height = 520, bg = 'black', relief = 'raised')
        canvas3.pack(side ="top",fill="both",expand="True")

        style=Style()

        style.configure('f.TButton', font =
               ('Helvetica', 20, 'bold'),
                foreground = 'black',background= 'black')
        style.configure('r.TButton', font =
               ('Helvetica', 10, 'bold'),
                foreground = 'red',background= 'black')
        style.configure('g.TButton', font =
               ('Helvetica', 10, 'bold'),
                foreground = 'green',background= 'black')
        
        style=Style()

        style.configure('gg.TButton', font =
               ('Helvetica', 10, 'bold'),
                foreground = 'black',background= 'black')

        label = ttk.Label(self, text="Flight Log CheckList", style='f.TButton')
        canvas3.create_window(325,24, window=label)

        import numpy as np

        def my_fun_1():
            z1=pd.read_csv('new_text.csv')
            for i in flight_status:
                z1.replace(to_replace = i, value = var[i].get(), inplace = True)
                
            option=['1']
            new_z = z1.loc[z1['Mode'].isin(option)]
            
            fault=pd.DataFrame(new_z,columns=basic_fault_col_names)
            phi=np.array(pd.DataFrame(new_z,columns=['Phi']).values.tolist())
            desired_phi=np.array(pd.DataFrame(new_z,columns=['Desired Phi']).values.tolist())

            the=np.array(pd.DataFrame(new_z,columns=['The']).values.tolist())
            desired_the=np.array(pd.DataFrame(new_z,columns=['Desired The']).values.tolist())

            psi=np.array(pd.DataFrame(new_z,columns=['Psi']).values.tolist())
            desired_psi=np.array(pd.DataFrame(new_z,columns=['Desired Psi']).values.tolist())
            controller_psi=np.array(pd.DataFrame(new_z,columns=['Controller Psi']).values.tolist())

            altitude=np.array(pd.DataFrame(new_z,columns=['Altitude']).values.tolist())
            desired_altitude=np.array(pd.DataFrame(new_z,columns=['Desired Altitude']).values.tolist())

            throttle=np.array(pd.DataFrame(new_z,columns=['Throttle']).values.tolist())
            
            voltage=np.array(pd.DataFrame(new_z,columns=['Voltage']).values.tolist())
            mid_voltage=np.array(pd.DataFrame(new_z,columns=['Mid-Voltage']).values.tolist())
            
            g1_sat=np.array(pd.DataFrame(new_z,columns=['G1 Sat']).values.tolist())
            g1_hdop=np.array(pd.DataFrame(new_z,columns=['G1 HDOP']).values.tolist())
            g2_sat=np.array(pd.DataFrame(new_z,columns=['G2 Sat']).values.tolist())
            g2_hdop=np.array(pd.DataFrame(new_z,columns=['G2 HDOP']).values.tolist())
            
            mag_field=np.array(pd.DataFrame(new_z,columns=['MAG Field']).values.tolist())
            i_az=np.array(pd.DataFrame(new_z,columns=['I Az']).values.tolist())

            mode=np.array(pd.DataFrame(df,columns=['Mode']).values.tolist())
            flight_time=np.array(pd.DataFrame(df,columns=['Flight Time']).values.tolist())


            #phi=phi.values.tolist()
            #phi=np.array(phi)
            #desired_phi=desired_phi.values.tolist()
            #desired_phi=np.array(desired_phi)

            '''
            labelh = ttk.Label(self, text=" Parameters ", style='gg.TButton')
            canvas3.create_window(100,150, window=labelh)

            labelt = ttk.Label(self, text=" FAIL/PASS ", style='gg.TButton')
            canvas3.create_window(200,150, window=labelt)

            labelp = ttk.Label(self, text=" Criteria ", style='gg.TButton')
            canvas3.create_window(300,150, window=labelp)
            '''
            label0 = tk.Label(self, text=" 1. Phi and Desired Phi ", bg='black',fg='white',width=20, font=SMALL_FONT)
            canvas3.create_window(125,100, window=label0)

            labelt = tk.Label(self, text=" 2. The and Desired The ", bg='black',fg='white',width=20, font=SMALL_FONT)
            canvas3.create_window(128,140, window=labelt)

            label4 = tk.Label(self, text=" 3. Psi and Desired Psi ", bg='black',fg='white',width=20, font=SMALL_FONT)
            canvas3.create_window(122,180, window=label4)

            label5 = tk.Label(self, text=" 4. Controller Psi and Psi ", bg='black',fg='white',width=20, font=SMALL_FONT)
            canvas3.create_window(128,220, window=label5)

            label6 = tk.Label(self, text=" 5. Alt and Desired Alt ", bg='black',fg='white',width=20, font=SMALL_FONT)
            canvas3.create_window(122,260, window=label6)

            label7 = tk.Label(self, text=" 6. Throttle ", bg='black',fg='white',width=20, font=SMALL_FONT)
            canvas3.create_window(100,300, window=label7)

            label8 = tk.Label(self, text=" 7. Volt and Mid-Volt ", bg='black',fg='white',width=20, font=SMALL_FONT)
            canvas3.create_window(120,340, window=label8)

            label9 = tk.Label(self, text=" 8. GPS A&B Satellites ", bg='black',fg='white',width=20, font=SMALL_FONT)
            canvas3.create_window(425,100, window=label9)

            label10 = tk.Label(self, text=" 9. GPS A&B HDOP Values ", bg='black',fg='white',width=20, font=SMALL_FONT)
            canvas3.create_window(425,140, window=label10)

            label11 = tk.Label(self, text=" 10. Motor PWM ", bg='black',fg='white',width=20, font=SMALL_FONT)
            canvas3.create_window(425,180, window=label11)

            label12 = tk.Label(self, text=" 11. Magnetic Field Value ", bg='black',fg='white',width=20, font=SMALL_FONT)
            canvas3.create_window(425,220, window=label12)

            label13 = tk.Label(self, text=" 12. I Az Vibration Value ", bg='black',fg='white',width=20, font=SMALL_FONT)
            canvas3.create_window(425,260, window=label13)

            label14 = tk.Label(self, text=" 13. FS_BATT initiated at ", bg='black',fg='white',width=20, font=SMALL_FONT)
            canvas3.create_window(425,300, window=label14)
            
            labela0 = ttk.Label(self, text=" ", style='r.TButton')
            canvas3.create_window(250,100, window=labela0)

            labela1 = ttk.Label(self, text=" ", style='r.TButton')
            canvas3.create_window(250,140, window=labela1)

            labela2 = ttk.Label(self, text=" ", style='r.TButton')
            canvas3.create_window(250,180, window=labela2)

            labela3 = ttk.Label(self, text=" ", style='r.TButton')
            canvas3.create_window(250,220, window=labela3)

            labela4 = ttk.Label(self, text=" ", style='r.TButton')
            canvas3.create_window(250,260, window=labela4)

            labela5 = ttk.Label(self, text=" ", style='r.TButton')
            canvas3.create_window(250,300, window=labela5)

            labela6 = ttk.Label(self, text=" ", style='r.TButton')
            canvas3.create_window(250,340, window=labela6)

            labela7 = ttk.Label(self, text=" ", style='r.TButton')
            canvas3.create_window(565,100, window=labela7)

            labela8 = ttk.Label(self, text=" ", style='r.TButton')
            canvas3.create_window(565,140, window=labela8)

            labela9 = ttk.Label(self, text=" ", style='r.TButton')
            canvas3.create_window(565,180, window=labela9)

            labela10 = ttk.Label(self, text=" ", style='r.TButton')
            canvas3.create_window(565,220, window=labela10)

            labela11 = ttk.Label(self, text=" ", style='r.TButton')
            canvas3.create_window(565,260, window=labela11)

            labela12 = ttk.Label(self, text=" None ", style='g.TButton')
            canvas3.create_window(565,300, window=labela12)

            '''
            def batt_command():
            import numpy as np
            data=df
            
            print(d)
            '''

            temp_phi = 0

            for i in range(len(desired_phi)):
                temp_phi+=(phi[i]-desired_phi[i])**2/len(desired_phi)
            temp_phi=np.sqrt(temp_phi)
            

            if (temp_phi> phi_overlapp):
                labela0['text']= "FAIL"
                labela0['style']='r.TButton'
            else:
                labela0['text']="PASS"
                labela0['style']='g.TButton'

            temp_the=0

            for i in range(len(desired_the)):
                temp_the+=(the[i]-desired_the[i])**2/len(desired_the)
            temp_the=np.sqrt(temp_the)
            

            if (temp_the > the_overlapp):
                labela1['text']= "FAIL"
                labela1['style']='r.TButton'
            else:
                labela1['text']="PASS"
                labela1['style']='g.TButton'

            temp_psi = 0

            for i in range(len(psi)):
                temp_psi += (psi[i]-desired_psi[i])**2/len(desired_psi)
            temp_psi = np.sqrt(temp_psi)

            if (temp_psi > psi_overlapp):
                labela2['text'] = "FAIL"
                labela2['style'] = 'r.TButton'
            else:
                labela2['text'] = "PASS"
                labela2['style'] = 'g.TButton'

            temp_yaw = 0
            temp_yaw=np.mean(controller_psi)
            
            if (np.abs(temp_yaw) < cont_psi_average):
                if (np.abs(np.mean(psi)) < 100):
                    labela3['text'] = "PASS"
                    labela3['style'] = 'g.TButton'
                else:
                    labela3['text'] = "FAIL"
                    labela3['style'] = 'r.TButton'

            else:
                labela3['text'] = "FAIL"
                labela3['style'] = 'r.TButton'
            temp_alt = 0

            for i in range(len(altitude)):
                temp_alt += (desired_altitude[i]-altitude[i])**2/len(altitude)
            temp_alt=np.sqrt(temp_alt)

            if (temp_alt > alt_overlapp):
                labela4['text'] = " FAIL "
                labela4['style'] = 'r.TButton'
                
            else:
                labela4['text'] = " PASS "
                labela4['style'] = 'g.TButton'

            if (np.max(throttle)> throttle_max):
                labela5['text'] = "FAIL"
                labela5['style'] = 'r.TButton'

            else:
                labela5['text'] = " PASS "
                labela5['style'] = 'g.TButton'

            temp_volt = 0

            voltage = np.delete(voltage,[0,1,2,3,4,5,6,7,8])
            for i in range(len(voltage)-1):
                print(np.abs(voltage[i+1]) - np.abs(voltage[i]))
                if ((np.abs(voltage[i+1])-np.abs(voltage[i])) > voltage_max*np.abs((np.max(voltage)-np.min(voltage))/len(voltage))):
                    temp_volt += 1
                if ((np.abs(voltage[i+1])-np.abs(voltage[i])) < voltage_max*np.abs((np.max(voltage)-np.min(voltage))/len(voltage))):
                    temp_volt -= 1
                    
            
            print(voltage_max*(np.max(voltage)-np.min(voltage))/len(voltage))

            
            if (temp_volt > 1):
                labela6['text'] = "FAIL"
                labela6['style'] = 'r.TButton'

            else:
                labela6['text'] = "    PASS    "
                labela6['style'] = 'g.TButton'

            if (np.min(g1_sat) < gps_min):
                labela7['text'] = "GPS A Loss"
                labela7['style'] = 'r.TButton'
                if (np.min(g2_sat) < gps_min):
                    labela7['text'] = "Both Loss"
                    labela7['style'] = 'r.TButton'
            
            if (np.min(g2_sat) < gps_min):
                labela7['text'] = "GPS B Loss"
                labela7['style'] = 'r.TButton'
                if (np.min(g1_sat) < gps_min):
                    labela7['text'] = "Both Loss"
                    labela7['style'] = 'r.TButton'
            else:
                labela7['text'] = "    PASS    "
                labela7['style'] = 'g.TButton'

            if (np.max(g1_hdop) > gps_hdop_max):
                labela8['text'] = "GPS A Loss"
                labela8['style'] = 'r.TButton'
                if (np.max(g2_hdop) > gps_hdop_max):
                    labela8['text'] = "Both Loss"
                    labela8['style'] = 'r.TButton'

            if (np.max(g2_hdop) > gps_hdop_max):
                labela8['text'] = "GPS B Loss"
                labela8['style'] = 'r.TButton'
                if (np.max(g2_hdop) > gps_hdop_max):
                    labela8['text'] = "Both Loss"
                    labela8['style'] = 'r.TButton'
            else:
                labela8['text'] = "    PASS    "
                labela8['style'] = 'g.TButton'

            if (np.max(g2_hdop) >= 180*gps_hdop_max):
                labela8['text'] = "GPS B FAIL"
                labela8['style'] = 'r.TButton'
                if (np.max(g1_hdop) >= 180*gps_hdop_max):
                    labela8['text'] = "Both FAIL"
                    labela8['style'] = 'r.TButton'

            if (np.max(g1_hdop) >= 180*gps_hdop_max):
                labela8['text'] = "GPS A FAIL"
                labela8['style'] = 'r.TButton'
                if (np.max(g2_hdop) >= 180*gps_hdop_max):
                    labela8['text'] = "Both FAIL"
                    labela8['style'] = 'r.TButton'
 
            temp_mag=0

            for i in range(len(mag_field)):
                temp_mag += mag_field[i]**2/len(mag_field)
            temp_mag=np.sqrt(temp_mag)

            if (temp_mag < mag_max):
                if (temp_mag > mag_min):
                    labela10['text'] = "PASS"
                    labela10['style'] = 'g.TButton'
                else:
                    labela10['text'] = "FAIL"
                    labela10['style'] = 'r.TButton'
                    
            else:
                labela10['text'] = "FAIL"
                labela10['style'] = 'r.TButton'

            temp_z=0

            for i in range(len(i_az)):
                temp_z += i_az[i]**2/len(i_az)
            temp_z=np.sqrt(temp_z)


            if (temp_z < iaz_max):
                labela11['text'] = "PASS"
                labela11['style'] = 'g.TButton'

            else:
                labela11['text'] = "FAIL"
                labela11['style'] = 'r.TButton'

            batt = str(0)


            for i in range(len(mode)):
                if (mode[i] == "FS_BATT"):
                    batt = (flight_time[i])
                    break

            batt=np.array_str(batt)

            labela12['text']=batt.replace('[',' ').replace(']',' ')
            print(batt)
            labela12['style'] = 'r.TButton'


        button= ttk.Button(self, text="Basic Flight Checks",style='r.TButton',
                            command=lambda: my_fun_1())
        canvas3.create_window(325,58, window=button)


        button1 = ttk.Button(self, text="Back to Home",style='r.TButton',
                            command=lambda: controller.show_frame(StartPage))
        canvas3.create_window(565,500, window=button1)

        button2 = ttk.Button(self, text="Comm Error Check",style='g.TButton',
                            command=lambda: controller.show_frame(PageOne))
        canvas3.create_window(325,480,window=button2)


class PageThree(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Graph Page!",bg='lightsteelblue',font=LARGE_FONT)
        label.pack(pady=1,padx=10)

        style=Style()

        style.configure('x.TButton', font =
               ('calibri', 10, 'bold', 'underline'),
                foreground = 'red') 
        button1 = ttk.Button(self, text="Back to Home",style='x.TButton',
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = ttk.Button(self, text="Refresh",
                            command=lambda: my_command())
        button2.pack()

        def my_command():
            canvas.get_tk_widget().pack_forget()
        
        
        '''
        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()
        
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        '''


app = iFapp()
#ani = animation.FuncAnimation(f, animate, interval=1000)
app.mainloop()


