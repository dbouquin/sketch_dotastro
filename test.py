from clarifai.rest import ClarifaiApp
import json 

app = ClarifaiApp(api_key='e4921122598d4dd381dd91893858fab4')

#app.inputs.create_image_from_url(url='http://www.perezmedia.net/beltofvenus/archives/images/2009/img2009082601_Jupiterlg.jpg', concepts=['Jupiter'])
#app.inputs.create_image_from_url(url='http://www.perezmedia.net/beltofvenus/archives/images/2005/img2005080202_Mars1.jpg', not_concepts=['not Jupiter'])

#model = app.models.create(model_id="Jupiter", concepts=["Jupiter"])

#model.train()

model = app.models.get('Jupiter')
res=model.predict_by_url('https://static.adsabs.harvard.edu/static/phaedra/phaedra0001/0000001.078.jpg')

print(res)
