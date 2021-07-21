from hash.utils.HashFile import HashFile
from django.shortcuts import render

# Create your views here.
def index(request):
    # hash = HashFile()
    # h = int(input(f"Entrez une valeur conprise {hash.q} et {hash.p} : "))
    # hash.parameter_generation(h)
    # hash.per_user_key()

    # hash.name=input("Enter the name of document to sign: ")
    # print(hash.signature())

    # print("r(Component of signature) is: ",hash.r)
    # print("k(Randomly chosen number) is: ",hash.k)
    # print("s(Component of signature) is: ",hash.s)

    # print()
    # print(hash.verification())
    return render(request, "index.html")


    hash = HashFile()
    h = int(input(f"Entrez une valeur conprise {hash.q} et {hash.p} : "))
    hash.parameter_generation(h)
    hash.per_user_key()

    hash.name=input("Enter the name of document to sign: ")
    print(hash.signature())

    print("r(Component of signature) is: ",hash.r)
    print("k(Randomly chosen number) is: ",hash.k)
    print("s(Component of signature) is: ",hash.s)

    print()
    print(hash.verification())