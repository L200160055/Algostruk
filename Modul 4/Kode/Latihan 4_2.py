def binSe(kumpulan,target):
    #Mulai dari seluruh runtutan elemen
    low=0
    high=len(kumpulan)-1

    #Secara berulang belah runtutan itu menjadi separuhnya sampai targetnya ditentukan
    while low<=high:
        #Temukan pertengahan runtutan tersebut
        mid=(high+low)//2
        #Apakah pertengahan memuat target?
        if kumpulan[mid]==target:
            return True
        #ataukah targetnya di sebelah kirinya?
        elif target<kumpulan[mid]:
            high=mid-1
        #ataukah targetnya di sebelah kananya?
        else:
            low=mid+1
        #Jika runtutan tidak bisa dibelah lagi, berarti targetnya tidak ada
    return False
