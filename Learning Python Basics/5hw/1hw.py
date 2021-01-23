f_obj=open("my_file.txt","a") #открыть файл
stop_word="@"
c=input("Input data here/ for exit input empty string\n")
while True:
    if stop_word in c:
        break
    else:
        f_obj.write(c)
        f_obj.write("\n")
        c = (input("Input data here/ for exit input empty string\n"))
f_obj.close() #close
