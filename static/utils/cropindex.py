def cpind(crop):
    crop_arr=['Arecanut', 'Rice', 'Banana', 'Turmeric', 'Maize', 'Sunflower',
            'Potato', 'Soyabean', 'Jute', 'Garlic', 'Onion', 'Papaya',
            'Ginger', 'Carrot', 'Mango', 'Pineapple', 'Cardamom', 'Coffee',
            'Brinjal', 'Grapes', 'Orange', 'Tomato', 'Cabbage']
    if crop in crop_arr:
        return crop_arr.index(crop)
    else:
        return 0

def seaind(season):
    season_arr=['Kharif', 'Whole Year', 'Autumn', 'Rabi','Summer', 'Winter']
    if season in season_arr:
        return season_arr.index(season)
    else:
        return 0