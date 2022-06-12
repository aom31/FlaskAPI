from flask import Flask 
from flask_restful import Api,Resource
#server side
app = Flask(__name__)
api=Api(app)

mycity={
    "bangkok":{"weather":"very hot", "temperature":40,"people":10000000},
    "nakornpatum":{"weather":"hot","temperature":"34", "people":3000000},
    "samutsakorn":{"weather":"rain","temperature":"27", "people":1000000},
    "samutprakarn":{"weather":"always rain","temperature":"24", "people":3000000},
    "pathumthani":{"weather":"cool","temperature":"20", "people":2000000},
    "chonburi":{"weather":"rain","temperature":"23", "people":4000000},
    "korat":{"weather":"very hot","temperature":"37", "people":5000000},
}
class WeatherCity(Resource):
    def get(self,name ):
        return mycity[name]
    #post method //input data
    def post(self,name):
        return {"data":"create resource ="+name}
    
#call
api.add_resource(WeatherCity, "/weather/<string:name>")
    
if __name__ == "__main__":
    app.run(debug=True)