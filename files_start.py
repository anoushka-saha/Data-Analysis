#Anoushka Saha
#Files Practice
#Python for Data Analysis
#July 10th, 2024

#Reading and writing files with the built-in Python file methods

def main():

    #open() - opening a file 
    #"w" - to be able to write to the file
    #"+" - tells python to create the file if it doesn't exist
    myfile = open("textfile.txt", "w+") 

    #Writing lines of data to file
    for i in range(10):
        myfile.write("This is some text\n")

    #Close the file when finished
    myfile.close()   

if __name__ == "__main__":
    main()