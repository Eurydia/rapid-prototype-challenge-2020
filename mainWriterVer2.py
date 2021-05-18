fieldLen = [
    2,
    10,
    4,
    3,
    4,
    2,
    5,
    5,
    6,
    4,
    2,
    4,
    4,
    16,
    17,
    4,
    4,
    5,
    21]

fieldNames = [
    'message type',
    'from (country)',
    'from (provider)',
    'event category',
    'event subcategory',
    'severity',
    'onset',
    'expected duration',
    'guidance library',
    'response guide',
    'instruction',
    'latitude',
    'longitude',
    'semi-major axis',
    'semi-minor axis',
    'azimuth',
    'parameter type']

fields = [
    ['alert',
     'update',
     'test',
     'cancel'],
    ['none'],
    ['none'],
    ['geo1',
     'geo2',
     'met1',
     'met2',
     'safety',
     'security',
     'transport',
     'fire'],
    [
        ['earthquake',
         'tsunami',
         'sinkhole',
         'avalanche',
         'satellite debris',
         'pyroclastic flow',
         'lava flow',
         'volcanic mud flow',
         'glacial ice avalanche',
         'tidal wave',
         'landslide'],
        ['debris flow',
         'ash fall',
         'volcanic eruption'],
        ['typhoon',
         'tornado',
         'storm',
         'hail',
         'dust storm',
         'storm surge',
         'heavy rain',
         'black ice',
         'high uv radiation',
         'plague of insects',
         'pest infestation',
         'epizootic',
         'contaminated drinking water'],
        ['heavy snow',
         'flood',
         'lightning',
         'extreme heat',
         'frost',
         'derecho',
         'fog',
         'snow drifts'],
        ['chemical hazard',
         'biological hazard',
         'radiological hazard',
         'nuclear hazard',
         'explosive hazard',
         'unidentified animal',
         'chemical accident',
         'hazardous material accident',
         'demonstration',
         'odour nuisance',
         'major event',
         'risk of infection',
         'noise pollution',
         'food safety alert',
         'safety warning'],
        ['shooting',
         'ballistic missile attack',
         'guerrilla attack',
         'large-scale terrorism',
         'air strike',
         'hijack',
         'chemical attack',
         'explosive attack',
         'nuclear weapon attack',
         'life threatening situation',
         'health hazard',
         'first/second world war bomb',
         'bomb discovery',
         'it system outage'],
        ['maritime disaster',
         'train accident',
         'bridge collapse',
         'aircraft crash',
         'oil spill',
         'road traffic accident',
         'traffic alert',
         'gas supply outage',
         'emergency number outage',
         'telephone line outage',
         'power outage'],
        ['forest fire',
         'structure fire',
         'solar storm',
         'missing person',
         'air pollution',
         'building collapse',
         'dam failure',
         'dike failure',
         'fire gases',
         'risk of fire',
         'gas leak',
         'nuclear power station accident',
         'raw sewage',
         'siren test',
         'warning',
         'acid rain']],
    ['extreme',
     'severe',
     'moderate',
     'minor'],
    ['none'],
    ['no duration',
     'duration < 0.25 hour',
     '0.25 <= duration < 0.5 hour',
     '0.5 <= duration < 0.75 hour',
     '0.75 <= duration < 1 hour',
     '1 <= duration < 1.5 hour ',
     '1.5 <= duration < 2 hour',
     '2 <= duration < 3 hour',
     '3 <= duration < 4 hour',
     '4 <= duration < 6 hour',
     '6 <= duration < 8 hour',
     '8 <= duration < 12 hour',
     '12 <= duration < 18 hour',
     '18 <= duration < 24 hour',
     '24 <= duration < 48 hour',
     '45 <= duration hour'],
    ['international guidance library',
     'national guidance library',
     'regional guidance library',
     'new guidance library under validation'],
    ['none'],
    ['test'],
    ['none'],
    ['none'],
    ['316',
     '635',
     '1277',
     '2565',
     '5154',
     '10355',
     '20806',
     '41803',
     '83993',
     '168761',
     '339081',
     '681292',
     '1368875',
     '2750388',
     '5526170',
     '11103363'],
    ['316',
     '635',
     '1277',
     '2565',
     '5154',
     '10355',
     '20806',
     '41803',
     '83993',
     '168761',
     '339081',
     '681292',
     '1368875',
     '2750388',
     '5526170',
     '11103363'],
    ['none'],
    ['none']
]

choice_picked_dec = []

choice_picked_bin = []


def question(question_index, question_title, **kwargs):
    index_pass = False

    display_choices = kwargs['display_choices_bool'] if not kwargs.get('display_choices_bool') is None else True

    question_choices = kwargs['question_choices_given'] if bool(kwargs.get('question_choices_given')) is True else None

    if question_choices is None:
        index_min, index_max = kwargs['question_min'], kwargs['question_max']

    else:
        try:
            index_min, *_, index_max = [value for value, _ in enumerate(question_choices)]

        except ValueError:
            index_min, index_max = 0, 0

    while index_pass is False:

        print(f'{question_index}. select {question_title}'.title())

        if display_choices is True:

            for choices_index, choice in enumerate(question_choices):
                print(f'\t| {choices_index}. {choice}'.title())

        try:
            index_picked = int(input(f'\nselect index (from {index_min} to {index_max}): '))

            choice_picked = question_choices[index_picked]

            choice_picked_dec.append(index_picked)

            print(f'\t*{choice_picked}* selected for {question_title}'.title())

            index_pass = True

        except TypeError:
            choice_picked_dec.append(index_picked)

            print(f'\t*{index_picked}* selected for {question_title}'.title())

            index_pass = True

        except Exception as error_c:
            print(f'\n\t{error_c}\n')

        finally:
            print('-' * 50)


def question_type_b(question_index, question_title, index_min, index_max):
    index_pass = False

    while index_pass is False:

        print(f'{question_index}. select {question_title}'.title())

        try:
            index_picked = int(input(f'\nselect index (from {index_min} to {index_max}): '))

            if float(index_max) >= index_picked >= float(index_min):

                choice_picked_dec.append(index_picked)

                print(f'\t*{index_picked}* selected for {question_title}'.title())

                index_pass = True

            else:
                print('\n\tlist index out of range\n')

                index_pass = False

        except Exception as error_c:
            print(f'\n\t{error_c}\n')

        finally:
            print('-' * 50)


for title_index, zipped in enumerate(zip(fieldNames, fields)):

    title, choices = zipped[0], zipped[1]

    if title_index == 3:

        confirm = False

        while confirm is False:
            question(title_index, title, question_choices_given=choices)

            preview = fields[title_index + 1][choice_picked_dec[-1]]

            print(f'preview for items in *{choices[choice_picked_dec[-1]]}*'.title())

            for choices_index_pre, choice_pre in enumerate(preview):
                print(f'\t| {choices_index_pre}. {choice_pre}'.title())

            confirm_ask = False

            while confirm_ask is False:
                try:
                    ask = int(input('are you sure (1/0): '))

                    if ask == 0:
                        choice_picked_dec.pop(-1)
                        confirm_ask = True

                    elif ask == 1:
                        confirm_ask = True
                        confirm = True

                    else:
                        choice_picked_dec.pop(-1)
                        print('\n\tError enter only 1 or 0\n')
                        confirm_ask = False

                except Exception as error:
                    choice_picked_dec.pop(-1)
                    print(f'\n\t{error}\n')

                finally:
                    print('-' * 50)

    elif title_index == 4:

        choices = choices[choice_picked_dec[-1]]

        question(title_index, title, question_choices_given=choices)

    elif title_index == 6:

        print(f'{title_index}. select onset'.title())

        index_sub = [6.1, 6.2, 6.3]
        title_sub = ['day', 'hour', 'minute']
        index_sub_range = [[0, 31], [0, 24], [0, 59]]

        for a, b, c in zip(index_sub, title_sub, index_sub_range):
            question(a, b, display_choices_bool=False, question_min=c[0], question_max=c[1])

    elif title_index == 11:
        question_type_b(title_index, title, '-90.000', '90.000')

    elif title_index == 12:
        question_type_b(title_index, title, '-180.000', '180.000')

    elif title_index == 15:
        question_type_b(title_index, title, '0', '180.00')

    else:
        question(title_index, title, question_choices_given=choices)

for index, zipped in enumerate(zip(choice_picked_dec, fieldLen)):
    picked, binary_len = zipped[0], zipped[1]

    if index == 13:
        order = int((picked + 90) / 0.0027466)
        picked_bin = bin(order)[2:]

    elif index == 14:
        order = int((picked + 180) / 0.0027466)
        picked_bin = bin(order)[2:]

    elif index == 17:
        order = int(picked / 5.806)
        picked_bin = bin(order)[2:]

    else:
        picked_bin = bin(picked)[2:]

    while len(picked_bin) < binary_len:
        picked_bin = f'0{picked_bin}'

    choice_picked_bin.append(picked_bin)

print(''.join(choice_picked_bin))
