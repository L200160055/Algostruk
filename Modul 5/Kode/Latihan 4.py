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

def selectionSort(a):
    n=len(a)
    for i in range(n-1):
        indexKecil=cariPosisiTerkecil(a,i,n)
        if indexKecil != i:
            swap(a,i,indexKecil)
