import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccount.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://plant-robot.firebaseio.com/'
})

ref = db.reference('/')
print(ref.get())

#from firebase import firebase
#
#url = "https://plant-robot.firebaseio.com/"
#fb = firebase.FirebaseApplication(url, None)
#plants = fb.get("/plant-robot", None)
#print(plants)