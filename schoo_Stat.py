

school_info = {
    'California State Monterey Bay' : { 'total_admitted':7576, 'total_admitted_male': 2343, 'total_admitted_female': 5233, 'grad_rate_4': 21, 'grad_rate_5': 46, 'grad_rate_6': 53},
    'San Diego State University': { 'total_admitted': 20321 , 'total_admitted_male': 8506, 'total_admitted_female': 11815, 'grad_rate_4': 30, 'grad_rate_5': 59, 'grad_rate_6': 68},
    'San Jose State University': { 'total_admitted': 16890, 'total_admitted_male':8022, 'total_admitted_female': 8868, 'grad_rate_4': 9, 'grad_rate_5': 39, 'grad_rate_6': 57},
    'California State Polytechnic': { 'total_admitted':13307, 'total_admitted_male': 6198, 'total_admitted_female': 7109, 'grad_rate_4': 15, 'grad_rate_5': 44, 'grad_rate_6': 63},
    'California State Long Beach':{ 'total_admitted':19650, 'total_admitted_male':7630, 'total_admitted_female':12020, 'grad_rate_4':16, 'grad_rate_5': 49, 'grad_rate_6': 67},
    'University of California Berkeley':{ 'total_admitted':13320, 'total_admitted_male':6082, 'total_admitted_female': 7238, 'grad_rate_4': 73, 'grad_rate_5': 89, 'grad_rate_6': 92},
    'University of California Davis': { 'total_admitted':24518, 'total_admitted_male': 9840, 'total_admitted_female': 14678, 'grad_rate_4': 58, 'grad_rate_5': 82, 'grad_rate_6': 85}
}

def school_data(school_info, college):
    stats = data[college]
    