# to append user_details to the file
def write_details():
  outfile = open("data.txt","a")
  fname = input("Please enter your first name: ")
  lname = input("Please enter your last name: ")
  addr = input("Please enter you address: ")
  contact = int(input("Please enter your phone number: "))
  profession = input("Please enter your profession: ")
  cont = str(contact)
  outfile.write("\n")
  outfile.write(fname)
  outfile.write("\t")
  outfile.write(lname)
  outfile.write("\n")
  outfile.write(addr)
  outfile.write("\n")
  outfile.write(cont)
  outfile.write("\n")
  outfile.write(profession)


  outfile.close()
write_details()



# to read user_details
outfile = open('data.txt',"r")
read = outfile.readlines()
modified = []

for line in read:
  modified.append(line.strip())
print(modified)

outfile.close()


# to delete data from the file
# toDel = open('data.txt', 'r+')
# toDel.seek(0)
# toDel.truncate()  

