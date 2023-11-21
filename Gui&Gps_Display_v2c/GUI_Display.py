import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk
from PIL import ImageTk,Image
import json
import sys
import webbrowser
if "tkinter" not in sys.modules:
    from tkinter import *
def open_location():
    webbrowser.open('gps_map.html')
def refresh():
    global temprature 
    global distance
    global fuel_level
    global BSA_state
    global longitude
    global latitude
    global FuelImageDirectory
    global bsa_image
    
    file = open('GUI_data.json')
    data = json.load(file)
    file.close()

    temprature = data['Temperature']
    distance = data['Elapsedtime']
    fuel_level = data['FuelLevel']
    BSA_state = data['BSA_state']
    longitude = data['longitude']
    latitude  = data['Latitude']
    
    ##update temp from file
    temp_label.config(text = ("Motor Temp: "+str(temprature)+"°C"))
    
    #Update distance
    dis_label.config(text = ("Distance: "+ str(distance) + " KM"))
    
    ##Update BSA from  
    if (BSA_state == 3):
        bsa_image = ImageTk.PhotoImage(Image.open("las/bsa_green.png"))
    else : 
        bsa_image = ImageTk.PhotoImage(Image.open("las/bsa_red.png"))
        
    bsa_label.configure (image = bsa_image)
    bsa_label.image = bsa_image
    
    ##update fuelLevel
    FuelImageDirectory = "las/" + str(fuel_level) +".png"
    fuel_image2 = ImageTk.PhotoImage(Image.open(FuelImageDirectory))
    fuel_label.configure (image = fuel_image2)
    fuel_label.image = fuel_image2
    mainWindow.after(5000, refresh) # run itself again after 1000 ms
    

def createGUI():
    global temprature 
    global distance
    global fuel_level
    global BSA_state
    global longitude
    global latitude
    global FuelImageDirectory
    global bsa_image
    global temp_label
    global dis_label
    global bsa_label
    global fuel_label
    global mainWindow
    ####void main 
    #main windo
    mainWindow = ttk.Window()
    mainWindow.title("V2C ADAS NEXUS")
    mainWindow.geometry("600x300")
    mainWindow.resizable(width = False,height = False)

     
    # Opening JSON file and reading data 
    file = open('GUI_data.json')
    data = json.load(file)
    file.close()

    temprature = data['Temperature']
    distance = data['Elapsedtime']
    fuel_level = data['FuelLevel']
    BSA_state = data['BSA_state']
    longitude = data['longitude']
    latitude  = data['Latitude']

    ##creating frames
    imageFrame = ttk.Frame(mainWindow)
    info_Frame = ttk.Frame(mainWindow)
    imageFrame.place(relx = .0,rely = .0 , relwidth = .4 , relheight = .9)
    info_Frame.place(relx = .42,rely = .1 , relwidth = .6 , relheight = .8)

    ##image frame
    FuelImageDirectory = "las/" + str(fuel_level) +".png"
    fuel_img    = ImageTk.PhotoImage(Image.open(FuelImageDirectory))
    fuel_label = ttk.Label(master = imageFrame,image = fuel_img)
    fuel_label.place(relx = 0,rely = 0 , relwidth = 1 , relheight = 1)

    ##all info frame
    details_Frame = ttk.Frame(info_Frame)
    buttonFrame = ttk.Frame(info_Frame)

    details_Frame.place(relx = .0,rely = .0 , relwidth = 1 , relheight = .6)
    buttonFrame.place(relx = .0,rely = .6 , relwidth = 1 , relheight = .4)


    ##temp and BSA Frame , Distance Freame
    bas_temp_frame = ttk.Frame(details_Frame)
    bas_temp_frame.place(relx = .0,rely = .0 , relwidth = .9 , relheight = .5)
    distance_frame = ttk.Frame(details_Frame)
    distance_frame.place(relx = .0,rely = .55, relwidth = .8 , relheight = .5)

    if (BSA_state == 3):
        bsa_image = ImageTk.PhotoImage(Image.open("las/bsa_green.png"))
    else : 
        bsa_image = ImageTk.PhotoImage(Image.open("las/bsa_red.png"))
        
    bsa_label = ttk.Label(master = bas_temp_frame , image = bsa_image)
    bsa_label.place(relx = .1,rely = .0 , relwidth = .30 , relheight = .8)


    temp_label = ttk.Label(master = bas_temp_frame , text = ("Motor Temp: "+str(temprature)+"°C"),font = 'Helvetica 15')
    temp_label.place(relx = .35,rely = .0 , relwidth = .6 , relheight = .8)


    dis_label = ttk.Label(master = distance_frame , text = ("Distance: "+ str(distance) + " KM"),font = 'Helvetica 15')
    dis_label.place(relx = .6 , anchor="center",  rely = .2 , relwidth = .8 , relheight = 1)

    #
        
    buttonStyle = ttk.Style()
    buttonStyle.configure('my.TButton', font=('Helvetica', 15))
    loction_button = ttk.Button( master = buttonFrame , text = 'open Location',style='my.TButton',command=open_location)
    loction_button.place(relx = .1,rely =.2  , relwidth = .68 , relheight = .5)
    refresh()


# run first time
createGUI()
#mainWindow.after(5000, refresh) # run itself again after 1000 ms
mainWindow.mainloop()
