
class skooma():
    def __init__(self,file_path, mode):
        print("init runs first")
        self.file_path = file_path
        self.mode = mode
        self.file = None
       
        
    def __enter__(self):
        print(" enter runs second")
        self.file = open(self.file_path, self.mode)
        return self.file
        
    def __exit__(self, *args):
        print("exit runs at the ... exit")
        for arg in args:
            print(arg, end=" ")
        print()
        self.file.close()
        

with skooma("file.txt","w") as f:
    f.write("some stuff")
    print("in with")