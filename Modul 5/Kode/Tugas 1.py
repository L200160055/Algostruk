class Manusia(object):
      keadaan='Lapar'
      def __init__(self,nama):
            self.nama=nama
      def ucapkansalam(self):
            print("salam, namaku",self.nama)
      def makan(self,s):
            self.keadaan='kenyang'
      def olahraga(self, k):
            print("Saya baru saja latihan",k)
            self.keadaan='lapar'
      def mengalikandengandua(self,n):
            return n*2
        
class mahasiswa(Manusia):
      def __init__(self,nama,NIM,kota,us):
            self.nama=nama
            self.NIM=NIM
            self.kotatinggal=kota
            self.uangsaku=us
      def __str__(self):
            s=self.nama + ', NIM '+str(self.NIM)\
               + ',  Tinggal di  '+self.kotatinggal\
               + ', Uang saku Rp '+str(self.uangsaku)\
               + ', tiap bulannya '
            return s
      def ambilNama(self):
            return self.nama
      def ambilNIM(self):
            return self.NIM
      def ambilUangSaku(self):
            return self.uangsaku
      def makan(self,s):
            print("Saya nbaru saja makan",s,"sambil tidur.")
            self.keadaan='kenyang'

class mhsTIF(mahasiswa):
    def katakanPy(self):
        print('Python is cool')
        
def swap(A,p,q):
    tmp=A[p]
    A[p]=A[q]
    A[q]=tmp

def cariPosisiTerkecil(A, dariSini, sampaiSini):
    posisiTerkecil=dariSini
    for i in range(dariSini+1, sampaiSini):
        if A[i] < A[posisiTerkecil]:
            posisiTerkecil=i
    return posisiTerkecil

def bubbleSort(a):
    n=len(a)
    for i in range(n-1):
        for j in range(n-i-1):
            if a[j] > a[j+1]:
                swap(a,j,j+1)

def selectionSort(a):
    n=len(a)
    for i in range(n-1):
        indexKecil=cariPosisiTerkecil(a,i,n)
        if indexKecil != i:
            swap(a,i,indexKecil)

def insertionSort(a):
    n=len(a)
    for i in range(1,n):
        nilai=a[i]
        pos=i
        while pos > 0 and nilai < a[pos-1]:
            a[pos]=a[pos-1]
            pos=pos-1
        a[pos] = nilai

def urutNIM(a):
    n=len(a)
    for i in range(n):
        nilai=a[i].NIM
        pos=i
        while pos > 0 and nilai < a[pos-1]:
            a[pos]=a[pos-1]
            pos=pos-1
        a[pos] = nilai

c0=mhsTIF('Ika',10,'Sukoharjo',240000)
c1=mhsTIF('Budi',51,'Sragen',230000)
c2=mhsTIF('Ahmad',2,'Surakarta',250000)
c3=mhsTIF('Chandra',18,'Surakarta',235000)
c4=mhsTIF('Eka',4,'Boyolali',240000)
c5=mhsTIF('fANDI',31,'Salatiga',250000)
c6=mhsTIF('Deni',13,'Klaten',245000)
c7=mhsTIF('Galuh',5,'Wonogiri',245000)
c8=mhsTIF('Janto',23,'Klaten',230000)
c9=mhsTIF('Hasan',64,'Karanganyar',270000)
c10=mhsTIF('Khalid',29,'Purwodadi',265000)
daftar=[c1,c2,c3,c4,c5,c6,c7,c8,c9,c10]
