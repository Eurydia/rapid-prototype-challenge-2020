from typing import List
from utils import (TYPE, COUNTRY, PROVIDER, CATEGORY, SERVERITY, DURATION, GUIDANCE_TO_REACT, RESPONSE, INSTRUCTION, PARAM_TYPE, POSITION, DEG_INTERVAL, AZIMUTH_INTERVAL)


def translate(lookup: List, index: int, default: str = 'none'):
    try: 
        return lookup[index]
    except IndexError:
        return default

def main():
    message = input()
    arr = []
    for index in POSITION:
        value = int(f'0b{message[:index]}', base=2)
        arr.append(value)
        message = message[index:]
        
    message_type = translate(TYPE, arr[0])
    country = COUNTRY.get(str(arr[1]), 'none')
    provider = translate(PROVIDER, arr[2])
    category, subcategory = translate(CATEGORY, arr[3])
    subcategory = translate(subcategory, arr[4])
    severity = translate(SERVERITY, arr[5])
    day = arr[6]
    hour = arr[7]
    minute = arr[8]
    duration = translate(DURATION, arr[9])
    guidance_lib = translate(GUIDANCE_TO_REACT, arr[10])
    response = translate(RESPONSE, arr[11])
    instruction = translate(INSTRUCTION, arr[12])
    longitude = -90 + (arr[13] * DEG_INTERVAL)
    latitude = -180 + (arr[14] * DEG_INTERVAL)
    s_major_axis = 10 ** (2.5 + (arr[15]/3.3))
    s_minor_axis = 10 ** (2.5 + (arr[16]/3.3))
    azimuth = arr[17] * AZIMUTH_INTERVAL
    param_type = translate(PARAM_TYPE, arr[18])

    print(f'Message Type: {message_type}')
    print(f'Country: {country}')
    print(f'Provider: {provider}')
    print(f'Category: {category}')
    print(f'Subcategory: {subcategory}')
    print(f'Severity: {severity}')
    print(f'Onset: {day} day {hour} hour {minute} minute')
    print(f'Expected Duration: {duration}') 
    print(f'Guidance Library: {guidance_lib}')   
    print(f'Response Guide: {response}')   
    print(f'Instruction: {instruction}')   
    print(f'Latitude: {latitude}')
    print(f'Longitude: {longitude}')
    print(f'Semi-Major Axis: {s_major_axis}')
    print(f'Semi-Minor Axis: {s_minor_axis}')
    print(f'Azimuth: {azimuth}')
    print(f'Parameter Type: {param_type}')
    
    input('Anykey to exit...')

if __name__ == '__main__':
    main()
    

