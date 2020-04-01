def cariPosisiYangTerkecil(A, dariSini, sampaiSini):
    posisiYangTerkecil=dariSini
    for i in range (dariSini+1, sampaiSini):
        if A[i]<A[posisiYangTerkecil]:
            posisYangTerkecil=i
    return posisiYangTerkecil
