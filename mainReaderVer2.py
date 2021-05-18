messageDigit = [
    [0, 2],
    [2, 12],
    [12, 16],
    [16, 19],
    [19, 23],
    [23, 25],
    [25, 41],
    [41, 45],
    [45, 47],
    [47, 51],
    [51, 55],
    [55, 71],
    [71, 88],
    [88, 92],
    [92, 96],
    [96, 101],
    [101, 122]
]

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

messageBinary, messageTranslated = [], []


def to_dec(binary):
    return int(binary, 2)


def translate(index):

    messageTranslated.append([])

    key = messageBinary[index]

    if index == 4:
        message = fields[index][to_dec(messageBinary[index-1])][to_dec(key)]

    elif index == 6:
        day = to_dec(key[:5])
        hour = to_dec(key[5:10])
        minute = to_dec(key[10:])
        message = f'{day} day(s) {hour} hour(s) {minute} minute(s)'

    elif index == 11:
        latitude = round(0.0027466 * to_dec(key) - 90, 3)
        message = f'{latitude} degree(s)'

    elif index == 12:
        longitude = round(0.0027466 * to_dec(key) - 180, 3)
        message = f'{longitude} degree(s)'

    elif index == 15:
        azimuth = round(5.8064516 * to_dec(key), 2)
        message = f'{azimuth} degree(s)'

    else:
        message = fields[index][0] if not fields[index][to_dec(key)] in fields[index] else fields[index][to_dec(key)]

    messageTranslated[-1].append(message.title())
    messageTranslated[-1].append(key)


def check():
    good = False
    while good is False:
        try:
            string = str(input('EWS message: '))
            print(len(string))
            main(string)
        except Exception as e:
            print(e)
            print('-' * 50)
        else:
            good = True


def main(message):
    for start, end in messageDigit:
        messageBinary.append(message[start:end])

    for field in range(17):
        translate(field)

    for name, translated in zip(fieldNames, messageTranslated):
        output = f'{name.title()}: {translated[0]} ({translated[1]})'
        print(output)


check()
