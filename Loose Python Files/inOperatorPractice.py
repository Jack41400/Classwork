fileList = ["myFile.txt",
            "myProgram.exe",
            "yourFile.txt",
            "basicCalculator.py"]

text = "hello, and welcome to my world."
x = text.capitalize()

print(x)

for fileName in fileList:
    if ".py" in fileName:
        print(fileName)
