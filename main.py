import os


template_text = ""
with open("template.html") as template:
    template_text = template.read()
        


text = ""

filenames = [filename for filename in os.listdir(os.getcwd()) if ".txt" in filename]
for i in range(len(filenames)):
   with open(os.path.join(os.getcwd(), filenames[i]), 'r', encoding="utf-8") as f: # open in readonly mode
        file_text = f.read()
        file_text = file_text.replace("\n","<br>")
        if i == 0:
            text+=f"<div class='carousel-item active'><div class='poem'><p>{file_text}</p></div></div>"
        else:
            text+=f"<div class='carousel-item'><div class='poem'><p>{file_text}</p></div></div>"
        print(filenames[i])

text = template_text.replace("<<>>", text)

output = open("output.html","w",encoding="utf-8")
output.write(text)