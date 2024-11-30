

class CocktailRecipe:
    def __init__(self,rec):        
        self.number = int(rec.pop(0)[1:])
        self.name = rec.pop(0)
        self.ref = rec.pop(0)
        self.link = rec.pop(0)
        
        ingredient_index = [i for i, s in enumerate(rec) if ';' in s]        
        self.ingredients = []
        self.units = []
        self.volumes = []
        for j in range(len(ingredient_index)):
            line = rec.pop(0)
            temp = line.split(';')                   
            self.ingredients.append(temp.pop(1).strip())            
            temp = temp.pop(0).split(' ')
            self.units.append(temp.pop(1))
            self.volumes.append(float(temp.pop(0)))
            
        index = [i for i, s in enumerate(rec) if 'Glass' in s]
        self.glass = rec.pop(index[0])            
        index = [i for i, s in enumerate(rec) if 'Ice' in s]
        self.ice = rec.pop(index[0])    
        index = [i for i, s in enumerate(rec) if 'Garnish' in s]
        self.garnish = rec.pop(index[0])
        self.preparation = rec.pop(0)
#         self.name = 'Old Fashioned'
#         self.volumes = [2, 1/4, 2]
#         self.units = ['oz','oz','dash']
#         self.ingredients = ['Whiskey','1.5:1 Simple Syrup','Angostura Bitters']
#         self.garnish = 'Orange Peel'
#         self.garnish_method = 'Express'
#         self.preparation = 'Stir'
        
    
    def disp(self):
        print(self.name)
        print('===============================')
        for i in range(len(self.ingredients)):
            print(f'{self.ingredients[i]:20} - {self.volumes[i]:5.3} {self.units[i]}')
        print(self.preparation)
        print(self.ice)
        print(self.glass)
        print(self.garnish)
#         print('Serve: ', self.ice, ' in ',self.glass)
#         print(f'Garnish: {self.garnish_method} {self.garnish}')
        print(f'{sum(self.volumes):5.3} ml ({sum(self.volumes)/29.5:4.2} oz)')
        print(f'{self.alcohol} ml alcohol')
        
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
    import pandas as pd
    
    unit_to_ml = {}
    volumes = pd.read_excel('Cocktails.xlsx',sheet_name='Volumes')
    for i in range(len(volumes)):
        unit_to_ml[volumes['Original'][i]] = volumes['ml'][i]
    #unit_to_ml = {'oz': 29.5, 'dash':0.9, 'dashes':0.9}
        
    abv = {}
    densities = pd.read_excel('Cocktails.xlsx',sheet_name='Density')
    for i in range(len(densities)):
        abv[densities['Ingredient'][i]] = densities['ABV'][i]
    #abv = {'Whiskey': 40, 'Angostura Bitters':44.7, '1.5:1 Simple Syrup':0, 'Water - Dilution':0, }
    
    with open('cocktailList.txt', encoding="utf-8") as f:
        read_data = f.read()
        
        lines = read_data.split('\n')
        lines = list(filter(None, lines))
        n_lines = len(lines)
        recipes = [i for i, s in enumerate(lines) if '#' in s]
    
        A = []
        for i in recipes:
            if i == recipes[len(recipes)-1]:
                j = n_lines
            else:
                j = recipes[recipes.index(i)+1]            
            recipe_in = lines[i:j]
            B = CocktailRecipe(recipe_in)
            B.convert_to_ml(unit_to_ml)
            B.dilute_cocktail()
            B.calculate_alcohol(abv)
            B.scale_volume(60)
            B.disp()
            
            A.append(B)
    