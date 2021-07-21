from hash.utils.HashFile import HashFile
from django.shortcuts import render

# Create your views here.

hasher = HashFile()


def generate_hash():
    print(f"p = {hasher.p} q = {hasher.q}")
    hasher.generate_mod_divider()

def index(request):
    hasher.signature()
    context = {"hasher": hasher}
    return render(request, "index.html", context)


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



def hash(request):
    generate_hash()
    # if request.method == "POST":
    #     hasher.parameter_generation(int(request.POST['h']))
    #     hasher.per_user_key()
    #     hasher.name = request.POST['path']
    #     print(request.POST['path'])

    return render(request, "hash.html", {"param": hasher})