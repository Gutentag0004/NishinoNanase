firstFile = open("C:\\Users\\gph\\workspace\\NishinoNanase\\nationalityproperty\\compareTask\\firstVersion.csv", 'rb')
secondFile = open("C:\\Users\\gph\\workspace\\NishinoNanase\\nationalityproperty\\compareTask\\secondVersion.csv", 'rb+')

for line in firstFile.readlines():
    csvFile.write(line)
    csvFile.flush()