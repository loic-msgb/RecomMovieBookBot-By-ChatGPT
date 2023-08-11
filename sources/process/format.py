import re
from datetime import timedelta

def extract_date(string):
    """
    Extract date from a string.

    Args:
        string (str): String to extract date from.
    
    Returns:
        str: Extracted date, or 'Date inconnue' if not found.
    """
    pattern = r'\((\d{4})\)'  # Utilisation de regex pour capturer une année entre parenthèses
    match = re.search(pattern, string)
    return match.group(1) if match and match.group(1) else 'Date inconnue'


def string_to_timedelta(duration_string):
    """
    Convertit une chaîne de caractères de durée au format "h hmin" en un objet timedelta.
    
    Args:
        duration_string (str): Chaîne de caractères de durée au format "h hmin".
        
    Returns:
        timedelta: Objet timedelta représentant la durée.
    """
    hours = 0
    minutes = 0
    hours_index = duration_string.find('h')
    
    if hours_index != -1:
        hours = int(duration_string[:hours_index])
        
        # Recherche des minutes après le 'h' mais en partant de l'index de 'h'
        minutes_index = duration_string.find('min', hours_index)
        if minutes_index != -1:
            minutes = int(duration_string[hours_index + 2:minutes_index])
    
    return timedelta(hours=hours, minutes=minutes)



def clean_scrapped_dict(data_dict):
    """
    Clean the scrapped dictionary to remove unwanted characters.

    Args:
        data_dict (dict): Scrapped dictionary.
    
    Returns:
        dict: Cleaned dictionary.
    """
    clean_dict = {}
    clean_dict['title'] = data_dict['title'].split(' ')[0]
    clean_dict['year'] = extract_date(data_dict['title'])
    clean_dict['duration'] = string_to_timedelta(data_dict['duration'])
    clean_dict['synopsis'] = data_dict['synopsis'].replace('\n', '').replace('\r', '').replace('\t', '').strip()

    return clean_dict

test_dict = {'title': 'Le Tombeau des lucioles (1988)', 'duration': ' 29 min', 'synopsis': "L'histoire tragique de l'adolescent Seita, de sa jeune sœur Setsuko et des luttes qu'ils mènent pour survivre au Japon de la Seconde Guerre Mondiale."} 
print(clean_scrapped_dict(test_dict))