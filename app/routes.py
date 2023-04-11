from flask import render_template
from app import app

@app.route('/')
def homePage():
    people = ['Shoha', 'Sarah', 'Aubrey', "Nicole"]

    more = {
        'hello': 'world'
    }

    return render_template('index.html', pop=people, more=more)

@app.route('/favorite5')
def favorite_5():
    favorite_artists = {
        'Glass Animals':'https://live-production.wcms.abc-cdn.net.au/20716664ffc92f5dd328ae42abd2bd8c?impolicy=wcms_crop_resize&cropH=562&cropW=1000&xPos=0&yPos=0&width=862&height=485',
        'Rex Orange County':'https://media.gq.com/photos/5db86b7fb2ccb20008b49804/4:3/w_4383,h_3287,c_limit/GQ-ROC-8.jpg',
        'The Beatles': 'https://yt3.googleusercontent.com/5lOkozHE7R-TL0iHNetrVWai47pG7Oa6bJvW4CiUGCMsRUjqXSUAlJWDgpkjdc12iKm0GwzF0Cw=s900-c-k-c0x00ffffff-no-rj',
        'Queen': 'https://www.anglotopia.net/wp-content/uploads/2017/06/Queen_band-800x500.jpg',
        'Lukas Graham':'https://i.scdn.co/image/ab6761610000e5eb0793531175d0f2f95cbb84ff',
    }

    test = {1:"a",2:"b"}


    return render_template('favorite5.html',favorite_artists=favorite_artists,test=test)