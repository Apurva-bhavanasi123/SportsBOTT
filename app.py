
def hello():

    import matplotlib.pyplot as plt
    import matplotlib.image as mpimg

    import urllib.request as r
    
    img = plt.imshow(mpimg.imread(r.urlopen("https://apiv2.apifootball.com/badges/logo_country/41_england.png")))
    print(img)
    
    
hello()
