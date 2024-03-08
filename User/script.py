
import sys 


def main(argv=sys.argv): 
    a=argv[1]
    b=argv[2]

    if a =="-t":
        print("hellow")
    
    if b =="-b":
        print("world")

if __name__=="__main__":
    main(argv=sys.argv)