TYPE = {
    '00' : 'alert',
    '01' : 'update',
    '10' : 'test',
    '11' : 'cancel'
}

COUNTRY = {
    '0000000000' : 'test'
}

PROVIDER = {
    '0000' : 'test'
}

CATEGORY = {
    '000' : 'geo1',
    '001' : 'geo2',
    '010' : 'met1',
    '011' : 'met2',
    '100' : 'safety',
    '101' : 'security',
    '110' : 'transport',
    '111' : 'fire'
}

SUBCLASS_GEO1 = {
    '0000' : 'earthquake',
    '0001' : 'tsunami',
    '0010' : 'sinkhole',
    '0011' : 'avalanche',
    '0100' : 'satellite debris',
    '0101' : 'pyroclastic flow',
    '0110' : 'lava flow',
    '0111' : 'volcanic mud flow',
    '1000' : 'glacial ice avalanche',
    '1001' : 'tidal wave',
    '1010' : 'landslide'
}

SUBCLASS_GEO2 = {
    '0000' : 'debris flow',
    '0001' : 'ash fall',
    '0010' : 'volcanic eruption'
}

SUBCLASS_MET1 = {
    '0000' : 'typhoon',
    '0001' : 'tornado',
    '0010' : 'storm',
    '0011' : 'hail',
    '0100' : 'dust storm',
    '0101' : 'storm surge',
    '0110' : 'heavy rain',
    '0111' : 'black ice',
    '1000' : 'high uv radiation',
    '1001' : 'plague of insects',
    '1010' : 'pest infestation',
    '1011' : 'epizootic',
    '1101' : 'contaminated drinking water'
}

SUBCLASS_MET2 = {
    '0000' : 'heavy snow',
    '0001' : 'flood',
    '0010' : 'lightning',
    '0011' : 'extreme heat',
    '0100' : 'frost',
    '0101' : 'derecho',
    '0110' : 'fog',
    '0111' : 'snow drifts'
}

SUBCLASS_SAFETY = {
    '0000' : 'chemical hazard',
    '0001' : 'biological hazard',
    '0010' : 'radiological hazard',
    '0011' : 'nuclear hazard',
    '0100' : 'explosive hazard',
    '0101' : 'unidentified animal',
    '0110' : 'chemical accident',
    '0111' : 'hazardous material accident',
    '1000' : 'demonstration',
    '1001' : 'odour nuisance',
    '1010' : 'major event',
    '1011' : 'risk of infection',
    '1101' : 'noise pollution',
    '1110' : 'food safety alert',
    '1111' : 'safety warning'
}

SUBCLASS_SECURITY = {
    '0000' : 'shooting',
    '0001' : 'ballistic missile attack',
    '0010' : 'guerrilla attack',
    '0011' : 'large-scale terrorism',
    '0100' : 'air strike',
    '0101' : 'hijack',
    '0110' : 'chemical attack',
    '0111' : 'explosive attack',
    '1000' : 'nuclear weapon attack',
    '1001' : 'life threatening situation',
    '1010' : 'health hazard',
    '1011' : 'first/second world war bomb',
    '1101' : 'bomb discovery',
    '1110' : 'it system outage'
}

message_subcategory_transport = {
    '0000' : 'maritime disaster',
    '0001' : 'train accident',
    '0010' : 'bridge collapse',
    '0011' : 'aircraft crash',
    '0100' : 'oil spill',
    '0101' : 'road traffic accident',
    '0110' : 'traffic alert',
    '0111' : 'gas supply outage',
    '1001' : 'emergency number outage',
    '1010' : 'telephone line outage',
    '1011' : 'power outage'
}

message_subcategory_fire = {
    '0000' : 'forest fire',
    '0001' : 'structure fire',
    '0010' : 'solar storm',
    '0011' : 'missing person',
    '0100' : 'air pollution',
    '0101' : 'building collapse',
    '0110' : 'dam failure',
    '0111' : 'dike failure',
    '1000' : 'fire gases',
    '1001' : 'risk of fire',
    '1010' : 'gas leak',
    '1011' : 'nuclear power station accident',
    '1100' : 'raw sewage',
    '1101' : 'siren test',
    '1110' : 'warning',
    '1111' : 'acid rain'
}

message_severity = {
    '00' : 'extreme',
    '01' : 'severe',
    '10' : 'moderate',
    '11' : 'minor'
}

message_expected_duration = {
    '0000' : 'no duration',
    '0001' : '< 0.25 hour',
    '0010' : '0.25 <= duration < 0.5 hour',
    '0011' : '0.5 <= duration < 0.75 hour',
    '0100' : '0.75 <= duration < 1 hour',
    '0101' : '1 <= duration < 1.5 hour ',
    '0110' : '1.5 <= duration < 2 hour',
    '0111' : '2 <= duration < 3 hour',
    '1000' : '3 <= duration < 4 hour',
    '1001' : '4 <= duration < 6 hour',
    '1010' : '6 <= duration < 8 hour',
    '1011' : '8 <= duration < 12 hour',
    '1100' : '12 <= duration < 18 hour',
    '1101' : '18 <= duration < 24 hour',
    '1110' : '24 <= duration < 48 hour',
    '1111' : '45 <= duration hour'
}

message_guidance_library = {
    '00' : 'international guidance library'
}

message_response_type = {
    '0111' : 'none'
}

message_guidance_intructions = {
    '0000' : 'test'
}

message_parameter = {

}