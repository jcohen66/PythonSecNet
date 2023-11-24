class MainClass:
    def message_main(self):
        print("This is from Main Class")


class MainClass2:
    def message_main2(self):
        print("This is from Main Class2")

class ChildClass(MainClass, MainClass2):
    def message(self):
        print("Welcome to Child Class")
        print("This is inherited from MainClass and MainClass2")

if __name__ == "__main__":
    child_obj = ChildClass()
    child_obj.message()
    child_obj.message_main()
    child_obj.message_main2()
