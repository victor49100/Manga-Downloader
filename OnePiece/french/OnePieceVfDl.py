
import requests # to get image from the web
import shutil # to save it locally
import os
import sys
## Set up the image URL and filename


arg = sys.argv

def DlOnePieceVf (Tome):
    dirname = ("OnePiece"+str(Tome))
    if not os.path.exists('OnePieceVf'):
        os.makedirs("OnePieceVf")

    os.chdir('OnePieceVf')
    if os.path.exists("OnePiece"+str(Tome)):
        os.chdir(dirname)
    else : 
        dirname = ("OnePiece"+str(Tome))
        os.mkdir(dirname)
        os.chdir(dirname)

    for page in range (1,300):
        if page<10:
            idp = str("0"+str(page))
        else:
            idp = page
            
        image_url = "https://one-piece-manga.fr/comic/"+str(Tome)+"/"+str(idp)+".jpg"
        filename = image_url.split("/")[-1]
        if page<10:
            filename = str(filename)
            filename = filename[1:]
        # Open the url image, set stream to True, this will return the stream content.
        r = requests.get(image_url, stream = True)
        # Check if the image was retrieved successfully
        if r.status_code == 200:
            # Set decode_content value to True, otherwise the downloaded image file's size will be zero.
            r.raw.decode_content = True
            # Open a local file with wb ( write binary ) permission.
            with open(filename,'wb') as f:
                shutil.copyfileobj(r.raw, f)
            print('Image sucessfully Downloaded: ',filename)
        else:
            image_url = "https://one-piece-manga.fr/comic/"+str(Tome)+"/"+str(idp)+".png"
            filename = image_url.split("/")[-1]
            if page<10:
                filename = str(filename)
                filename = filename[1:]
            r = requests.get(image_url, stream = True)
            if r.status_code == 200:
                r.raw.decode_content = True
                with open(filename,'wb') as f:
                    shutil.copyfileobj(r.raw, f)
                print('Image sucessfully Downloaded: ',filename)
            else:
                image_url = "https://one-piece-manga.fr/comic/"+str(Tome)+"/"+str(idp)+".webp"
            filename = image_url.split("/")[-1]
            r = requests.get(image_url, stream = True)
            if r.status_code == 200:
                r.raw.decode_content = True
                with open(filename,'wb') as f:
                    shutil.copyfileobj(r.raw, f)
            else:
                print('Manga not found',image_url)
                print ("fin :"+str((page-1))+" pages tétéchargé")
                break

            
print(DlOnePieceVf(1050))
