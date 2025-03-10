from crewai_tools import FileWriterTool


writer = FileWriterTool()

contenu ='bonjour les amis comment allez-vous'

print(contenu)

result = writer.run(content=contenu,filename="example.txt",overwrite="True")

print ("final")

print(result)

