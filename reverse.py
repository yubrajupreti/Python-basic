class Reverse:
    def __init__(self,sentence="hello buddy"):
        self.sentence=sentence

    def reverse(self):
        return "".join(self.sentence[::-1])   


if __name__=="__main__":
    sentence=input("enter the sentence to be reversed")
    reverse_sentence=Reverse(sentence)
    print("the reverse sentence is",reverse_sentence.reverse())         