from utils import (TYPE, CATEGORY, SERVERITY, DURATION, AXIS, POSITION, DEG_INTERVAL, AZIMUTH_INTERVAL)

def ask_with_choice(title: str, lookup) -> str:
    print(title)
    limit = len(lookup) - 1
    for i, data in enumerate(lookup):
        print(f'\t{i}. {data}')
    while True:
        try:
            answer = int(input(f'select index (from 0 to {limit}): '))
            assert limit >= answer >= 0
            return answer
        except AssertionError:
            print('Invalid input.')

def ask_with_limit(title, limit: int, lower_bound = 0):
    print(title)
    while True:
        try:
            answer = int(input(f'select index (from {lower_bound} to {limit}): '))
            assert limit >= answer >= lower_bound
            return answer
        except AssertionError:
            print('Invalid input.')

def ask_with_backtrack(title, lookup):
    print(title)
    limit = len(lookup) - 1
    for i, data in enumerate(lookup):
        print(f'\t{i}. {data[0]}')
    while True:
        try:
            answer = int(input(f'select index (from 0 to {limit}): '))
            assert limit >= answer >= 0

            _, next_question = lookup[answer]
            for i, data in enumerate(next_question):
                print(f'\t{i}. {data}')

            confirm = input('Are you sure with your choice (y/n): ')
            if confirm.lower() == 'y':
                return answer, next_question
        except AssertionError:
            print('Invalid input.')

def ask(title: str) -> str:
    print(title)
    answer = int(input('select index (from 0 to any): '))
    return answer

def main():
    message_type = ask_with_choice('Type', TYPE)
    country = ask('Country')
    provider = ask('Provider')
    category, subcategory = ask_with_backtrack('Category', CATEGORY)
    subcategory = ask_with_choice('Subcategory', subcategory)
    severity = ask_with_choice('Severity', SERVERITY)
    day = ask_with_limit('day', 31)
    hour = ask_with_limit('hour', 24)
    minute = ask_with_limit('minute', 59)
    duration = ask_with_choice('Duration', DURATION)
    guidance_lib = ask('Guidance lib')
    response = ask('Response')
    instruction = ask('Instruction')
    longitude = ask_with_limit('Longitude', 90, -90)
    latitude = ask_with_limit('Latitude', 180, -180)
    s_major_axis = ask_with_choice('Semi-major axis', AXIS)
    s_minor_axis = ask_with_choice('Semi-minor axis', AXIS)
    azimuth = ask_with_limit('Azimuth', 180)
    param_type = ask('parameter type')

    prepare_for_binary = [
        message_type,
        country,
        provider,
        category,
        subcategory,
        severity,
        day,
        hour,
        minute,
        duration,
        guidance_lib,
        response,
        instruction,
        longitude,
        latitude,
        s_major_axis,
        s_minor_axis,
        azimuth,
        param_type
    ]
    print(prepare_for_binary)
    binary = ''
    for i, zipped in enumerate(zip(prepare_for_binary, POSITION)):
        d, l = zipped
        if i == 13:
            d = (d + 90) // DEG_INTERVAL
        elif i == 14:
            d = (d + 180) // DEG_INTERVAL
        elif i == 17:
            d = d // AZIMUTH_INTERVAL

        binary += bin(int(d))[2:].zfill(l)
    print(binary)
    

if __name__ == '__main__':
    main()
