# IMPORTS

import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageDraw, ImageFont
import re





# FUNCTIONS

def retrieveInput():
    writtenWork = textBox.get("1.0",'end-1c')
    #print(writtenWork)
    return writtenWork



def retrieveFileName():
    fileInfo = file_input.get()
    if fileInfo == "":
        fileInfo = "ScratchWriter-"
    return fileInfo



def fontGenerate(name, size):
    return ImageFont.truetype(f"{name}.ttf", size)



def lineWrap(bumbFic, lineMax):
    bumbArray = re.split("\n", bumbFic)
    printArray = []
    lineLengthMax = lineMax

    for paragraph in bumbArray:
        bumbWords = re.split(" ", paragraph)
        lineWord = 0
        while lineWord != len(bumbWords):
            lineLength = 0
            lineContent = ""
            while lineLength <= lineLengthMax:
                if len(lineContent) == 0:
                    lineContent = bumbWords[lineWord]
                    lineLength += len(bumbWords[lineWord])
                else:
                    lineContent = lineContent + " " + bumbWords[lineWord]
                    lineLength += len(bumbWords[lineWord])
                    lineLength += 1 #For space bar
                
                if lineLength > lineLengthMax:
                    lineLength -= len(bumbWords[lineWord])
                    lineLength -= 1 #For space bar
                    lineContent = lineContent[:lineLength]
                    break
            
                lineWord += 1
                if lineWord == len(bumbWords):
                    break
                
            printArray.append(lineContent)
            #print(f"Line Content: {lineContent} w/ {lineLength}")
        lineLength = 0
        lineContent = ""
        #printArray.append(lineContent)
        #print(f"Line Content: {lineContent} w/ {lineLength}")
    return printArray



def generateImages(showOrSave):
    bumbFic = retrieveInput()

    if bumbFic == '':
        return

    if showOrSave == "Save":
        root.directory = filedialog.askdirectory()
        if root.directory == "":
            return
    
    printArray = lineWrap(bumbFic, 39)

    textSize = 23
    printLine = 0
    imageNum = 0

    sans = fontGenerate("Arial", textSize)
    #Comic Sans MS (40, -5), Arial Unicode (40, -5), Arial (39, 0)

    while printLine != len(printArray):
        img = Image.new(mode="RGBA", size=(480,360), color=(0,0,0,0))
        draw = ImageDraw.Draw(img)
    
        curlY = 0 # Could also be -5
        loop = 0
    
        while loop < 12:
            draw.text(xy=(10,curlY), text=printArray[printLine],
                      size=textSize, font=sans, fill=(0,0,0))
            curlY += 30
            printLine += 1
            loop += 1
            if printLine == len(printArray):
                break

        imageNum += 1
        fileNamePrint = retrieveFileName()
        finalName = f"{fileNamePrint}{imageNum}.png"
        if showOrSave == "Save":
            finalNameFinal = f"{root.directory}/{finalName}"
        #print(finalNameFinal)

        #MAKE THIS .SAVE TO DOWNLOAD, .SHOW FOR TESTING
        if showOrSave == "Show":    
            img.show(finalName)   
        if showOrSave == "Save":    
            img.save(finalNameFinal, 'PNG') 









# TKINTER CODE

root = tk.Tk()
root.title('ScratchWriter')

titleLabel = tk.Label(root, text='Welcome to ScratchWriter 0.0!')
titleLabel.pack()

instLabel = tk.Label(root, text='In the space below, paste your writing.')
instLabel.pack()

textBox = tk.Text(root, height=10, width=60)
textBox.pack()
textBox.insert(tk.END, '')

fileTitle = tk.Label(root, text='Put the base file name you want for your images.')
fileTitle.pack()
fileTitle2 = tk.Label(root, text="They'll be saved as {your name}1.png, {your name}2.png, etc.")
fileTitle2.pack()
file_input = tk.StringVar(root)
fileName = tk.Entry(root, textvariable=file_input)
fileName.pack()

#button = tk.Button(root, text='Preview Images', width=25, command=lambda: generateImages("Show"))
#button.pack()

button2 = tk.Button(root, text='Download Images', width=25, command=lambda: generateImages("Save"))
button2.pack()

root.mainloop()
