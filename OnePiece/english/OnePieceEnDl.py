import requests # to get image from the web
import shutil # to save it locally
import os
import sys
import Url
## Set up the image URL and filename

def DlOnePieceVf ():
    Tome = int(input("Which chapter is your download?: ")) 
    if not os.path.exists('One_PieceEn'):
        os.makedirs("One_PieceEn")
    os.chdir('One_PieceEn')
    if os.path.exists("OnePieceEn"+str(Tome)):
        os.chdir("OnePieceEn"+str(Tome))
    else:
        os.makedirs("OnePieceEn"+str(Tome))
        os.chdir("OnePieceEn"+str(Tome))


    for page in range (1,300):
        image_url = Url.ConvertUrlToTome(Tome)
        if Tome > 1049:
            if page <2:
                image_url = image_url.replace("X",("0"+str(page)))
            if page > 1 and page < 10:
                image_url = image_url.replace("X",("00"+str(page)))
            if page > 9:
                image_url = image_url.replace("X",("0"+str(page)))

        else:
            image_url = image_url.replace("X",str(page))
        filename = image_url.split("/")[-1]
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
        else :
            print('Manga not found',image_url)
            break

print(DlOnePieceVf())
