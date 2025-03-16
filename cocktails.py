class CocktailRecipe:
    from types import SimpleNamespace
    def __init__(self, data):
        # Expecting JSON data
        #         {
        #         "name": "Old Fashioned",
        #             "link": "https://www.youtube.com/watch?v=mf1ax7y0yyI",
        #             "reference": "How to Drink",
        #             "ingredients": [
        #             { "val": 2, "unit": "oz", "type": "Whiskey"},
        #             { "val": 25, "unit": "oz", "type": "1.5:1 Simple Syrup"},
        #             { "val": 4, "unit": "dashes", "type": "Angostura Bitters"}
        #             ],           
        #             "ice": "1 Large Lump",
        #             "glass": "Rocks",
        #             "garnish": "Express Orange Peel",
        #             "directions": [
        #             {"step": 1, "val": "Stir"}
        #             ]
        #         }
        self.iput = data
        self.name = data['name']
        self.ref = data['reference']
        self.link = data['link']
        self.ingredients = []
        self.volumes = []
        self.units = []
        self.ice = data['ice']
        self.glass = data['glass']
        self.garnish = data['garnish']
        self.directions = [];
        
        for i in data['ingredients']:
            self.ingredients.append(i['type'])
            self.volumes.append(float(i['val']))
            self.units.append(i['unit'])
        
        for i in data['directions']:
            self.directions.append(i['val'])
    
    
    def disp(self):
        print(self.name)
        print('===============================')
        for i in range(len(self.ingredients)):
            print(f'{self.ingredients[i]:20} - {self.volumes[i]:5.3} {self.units[i]}')
        print(f'ice:   {self.ice}')
        print(f'glass: {self.glass}')
        print(f'with:  {self.garnish}')
        for i in range(len(self.directions)):
            print(f'{i+1:2}. {self.directions[i]}')
        print('===============================')
        print(f'{sum(self.volumes):5.3} ml ({sum(self.volumes)/29.5:4.2} oz)')
        #print(f'{self.alcohol} ml alcohol')
        
    def convert_to_ml(self,unit_to_ml):
        for i in range(len(self.ingredients)):
            self.volumes[i] = self.volumes[i]*unit_to_ml[self.units[i]]/100
            self.units[i] = 'ml'
            
    def calculate_alcohol(self, abv):
        self.alcohol = 0
        for i in range(len(self.ingredients)):
            self.alcohol = self.alcohol + self.volumes[i]*abv[self.ingredients[i]]
            
    def dilute_cocktail(self):
        volume = sum(self.volumes)
        dilution = 0.2*volume
        self.ingredients.append('Water - Dilution')
        self.volumes.append(dilution)
        self.units.append('ml')
        
    def scale_volume(self, v_target):
        volume = sum(self.volumes)
        scale_factor = v_target / volume;
        for i in range(len(self.ingredients)):
            self.volumes[i] = self.volumes[i]*scale_factor
        
            

if __name__ == "__main__":
    import json

    # Opening JSON file
    f = open('cocktailList.json')

    # returns JSON object as a dictionary
    data = json.load(f)

    # Iterating through the json list
    for i in data['cocktails']:
        print(i)

    # Closing file
    f.close()