# from Crypto.Util.number import *
# from Crypto.Util.number import *
from Crypto.Util.number import *
from random import *
from hashlib import sha1

class HashFile():

    p = 0
    q = 0
    g = 0

    x = 0
    y = 0

    r = 0
    s = 0
    k = 0
    name = ""
    # names = ""
    hash = ""

    def __init__(self) -> None:
        self.generate_mod_divider()
        # print('Hello Word')

        
    # Hachage du message en SHA1
    def hash_function(self, message):
        hashed=sha1(message.encode("UTF-8")).hexdigest()
        return hashed

    # Inverse Multiplicative Modulaire
    def mod_Inverse(self, a, m) :
        a=a%m
        for x in range(1,m) :
            if((a*x)%m==1) :
                return(x)
        return(1)

    
    def generate_mod_divider(self):
        self.q = getPrime(5)
        self.p = getPrime(5)

        while((self.p-1)%self.q!=0):
            self.p=getPrime(10)
            self.q=getPrime(5)

    # les paramètres globaux sont q,p et g
    def parameter_generation (self, h):

            
        flag=True
        while(flag):
            # h=int(input("Enter integer between 1 and p-1(h): "))
            # h doit être compris entre 1 et p-1
            if(1<h<(self.p-1)):
                self.g=1
                while(self.g==1):
                    self.g=pow(h,int((self.p-1)/self.q))%self.p
                flag=False
        #     else:
        #         print("wrong entry")
        # print("Value of g is : ",g)

        # returning then as they are public globally
        # return(p,q,g)
        
                
    def per_user_key(self):

        # User private key:
        self.x=randint(1,self.q-1)
        # print("Randomly chosen x(Private key) is: ",x)

        # User public key:
        self.y=pow(self.g,self.x)%self.p
        # print("Randomly chosen y(Public key) is: ",y)

        # returning private and public components
        # return(x,y)

    def signature(self):
        hash_component = ""
        with open(self.name) as file:
            text=file.read()
            hash_component = self.hash_function(text)
            # print("Hash of document sent is: ",hash_component)
        self.r=0
        self.s=0
        while(self.s==0 or self.r==0):
            self.k=randint(1,self.q-1)
            self.r=((pow(self.g,self.k))%self.p)%self.q
            i=self.mod_Inverse(self.k,self.q)

            # converting hexa decimal to binary
            hashed=int(hash_component,16)
            self.s=(i*(hashed+(self.x*self.r)))%self.q

        # returning the signature components
        # return(r,s,k)
        self.hash = hash_component
        return hash_component


    def verification(self):
        with open(self.name) as file:
            text=file.read()
            hash_component = self.hash_function(text)
            # print("Hash of document received is: ", hash_component)

        # computing w
        w=self.mod_Inverse(self.s,self.q)
        # print("Value of w is : ",w)

        hashed=int(hash_component,16)

        # computing u1, u2 and v
        u1=(hashed*w)%self.q
        u2=(self.r*w)%self.q
        v=((pow(self.g,u1)*pow(self.y,u2))%self.p)%self.q

        # print("Value of u1 is: ",u1)
        # print("Value of u2 is: ",u2)
        # print("Value of v is: ",v)

        if(v==self.r):
            return True
        else:
            return False