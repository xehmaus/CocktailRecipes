

class CocktailRecipe:
    def __init__(self):
        self.name = 'Old Fashioned'
        self.volumes = [2, 1/4, 2]
        self.units = ['oz','oz','dash']
        self.ingredients = ['Whiskey','1.5:1 Simple Syrup','Angostura Bitters']
        self.garnish = 'Orange Peel'
        self.garnish_method = 'Express'
        self.preparation = 'Stir'
        self.glass = 'Rocks'
        self.ice = 'Lump'
        
    
    def disp(self):
        print(self.name)
        print('===============================')
        for i in range(len(self.ingredients)):
            print(f'{self.ingredients[i]:20} - {self.volumes[i]:5.3} {self.units[i]}')
        print(self.preparation)
        print('Serve: ', self.ice, ' in ',self.glass)
        print(f'Garnish: {self.garnish_method} {self.garnish}')
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
    
    unit_to_ml = {'oz': 29.5, 'dash':0.9}
    abv = {'Whiskey': 40, 'Angostura Bitters':44.7, '1.5:1 Simple Syrup':0, 'Water - Dilution':0}
    A = CocktailRecipe()
    A.convert_to_ml(unit_to_ml)
    A.dilute_cocktail()
    A.calculate_alcohol(abv)
    A.scale_volume(60)
    A.disp()
    