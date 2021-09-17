from iso3166 import countries

TYPE = ('alert', 'update', 'test', 'cancel')
COUNTRY = {y[0]:y[1] for y in sorted(((x.numeric, x.name) for x in countries), key=lambda x: int(x[0]))}
PROVIDER = ('none', )
CATEGORY = (
    ('geo1', (
        'earthquake',
        'tsunami',
        'sinkhole',
        'avalanche',
        'satellite debris',
        'pyroclastic flow',
        'lava flow',
        'volcanic mud flow',
        'glacial ice avalanche',
        'tidal wave',
        'landslide'
        )
    ), 
    ('geo2', (
        'debris flow',
        'ash fall',
        'volcanic eruption'
        )
    ), 
    ('met1', (
        'typhoon',
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
        'contaminated drinking water'
        )
    ), 
    ('met2', (
        'heavy snow',
        'flood',
        'lightning',
        'extreme heat',
        'frost',
        'derecho',
        'fog',
        'snow drifts'
        ),
    ), 
    ('safety', (
        'chemical hazard',
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
        'safety warning'
        )
    ), 
    ('security', (
        'shooting',
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
        'it system outage'
        )
    ),
    ('transport', (
        'maritime disaster',
        'train accident',
        'bridge collapse',
        'aircraft crash',
        'oil spill',
        'road traffic accident',
        'traffic alert',
        'gas supply outage',
        'emergency number outage',
        'telephone line outage',
        'power outage'
        )
    ), 
    ('fire', (
        'forest fire',
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
        'acid rain'
        )
    )
)
SERVERITY = ('extreme', 'severe', 'moderate', 'minor')
DURATION = ('no duration',
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
    '45 <= duration hour'
    )
GUIDANCE_TO_REACT = ('international guidance library',
    'national guidance library',
    'regional guidance library',
    'new guidance library under validation'
    )
AXIS = (
    316,
    635,
    1277,
    2565,
    5154,
    10355,
    20806,
    41803,
    83993,
    168761,
    339081,
    681292,
    1368875,
    2750388,
    5526170,
    11103363
    )
RESPONSE = ('none', )
INSTRUCTION = ('none', )
PARAM_TYPE = ('none', )

DEG_INTERVAL = 180/((2**16)-1)
AZIMUTH_INTERVAL = 180/((2**5)-1)
POSITION = (2, 10, 4, 3, 4, 2, 5, 5, 6, 4, 2, 4, 4, 16, 17, 4, 4, 5, 21)

