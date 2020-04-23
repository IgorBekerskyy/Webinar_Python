from abc import ABC, abstract method


class AbstractParent(ABC):
    @abstractmethod
    def hello_friend():
        raise NotImplementedError


class Mother(AbstractParent):
    def init(self, age=):
        self.age = age
        print('Mother constructor!')

    def do_work(self):
        print("I'm working")

        def do_house_work(self):
            print("Im listening music")


class Father(AbstractParent):
    def init(self):
        print('Father constructor!')

    def play_guitar(self):
        print('play guitar')

    def do_house_work(self):
        print ("sitting on the sofa and drink beer")


class Daughter(Mother, Father):

    def init(self, age=0):
        Mother.init(self, age=age)
        Father.init(self)

    def do_work(self):
        print("I'm working like a horse!")
    def dont_do_work_and_relax_in_room(self):
        print ("Im going to my room ")

    def hello_friend(self):
        pass

    class Friend:
        pass


def greet_mother(mother: Mother):
    print("Hello mother!!!")
    mother.do_work()


def greet_father(father: Father):
    print('time to beer!')
    father.play_guitar()

    if __name__ == "__main__":
        daughter==Daughter()
        #mother.do_work()


        greet_mother(daughter)
        greet_father(daughter)
        daughter.hello_friend()
        daughter.do_house_work
        daughter.dont_do_work_and_relax_in_room()








    for x in [daughter] :
        x.do_house_work ()
    #tuple
    vasian = ("11 years",11 ,3,14, daughter)

    #set
    my_set={ 23,11,10 }

    #list
    povtorka_list =["mathan_2","programming2", "superprise"]

    #frozen set
    another_set= frozenset(["di","mi","do"])


