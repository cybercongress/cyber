import math


def p_inflation(params, substep, state_history, previous_state):
    S = previous_state['T'] + previous_state['F'] + previous_state['L']
    L_r = previous_state['L']/S
    IRC = (1 - (L_r/params['goalVested'])) * params['inflationRateChange']
    IRC = IRC / params['unitsPerYear']
    return {'IRC': IRC}


def p_provision(params, substep, state_history, previous_state):
    S = previous_state['T'] + previous_state['F'] + previous_state['L']
    L_r = previous_state['L'] / S
    IRC = ((1 - L_r/params['goalVested']) * params['inflationRateChange']) / params['unitsPerYear']
    I_r = previous_state['I_r'] + IRC
    if I_r > params['inflationMax']:
        I_r = params['inflationMax']
    elif I_r < params['inflationMin']:
        I_r = params['inflationMin']
    I_p = (S * I_r) / params['unitsPerYear']
    return {'provision': math.floor(I_p)}


def p_claim(params, substep, state_history, previous_state):
    delta_f = (5.6 * 10**14) / (3 * params['unitsPerYear'])
    if previous_state['F'] <= 0:
        delta_f = 0
    return {'delta_F': -delta_f}


def p_vest(params, substep, state_history, previous_state):
    investmint = previous_state['T']/((params['unitsPerYear']/12) * params['vestingSpeed'])
    return {'delta_L': math.floor(investmint)}


def p_unvest(params, substep, state_history, previous_state):
    if previous_state['timestep'] <= params['baseVestingTime']:
        uninvestmint = 0
    else:
        uninvestmint = previous_state['T']/((params['unitsPerYear']/12) * params['unvestingSpeed'])
    return {'delta_U': math.floor(uninvestmint)}


def p_mr_a(params, substep, state_history, previous_state):
    x = previous_state['timestep'] // params['unitsPerYear']
    d_mr = params['MRa'] / (2**x)
    return {'delta_MRa': d_mr}


def p_mr_v(params, substep, state_history, previous_state):
    x = previous_state['V'] // params['voltHalving']
    d_mr = params['MRv'] / (2**x)
    return {'delta_MRv': d_mr}


def p_cl(params, substep, state_history, previous_state):
    if previous_state['timestep'] % (params['unitsPerYear']/365) == 0:
        # years = 10 * params['unitsPerYear']
        # ratio = 45 / years
        # util_rate = (5 + ratio) * previous_state['timestep']
        # util_rate *= 0.01
        #
        # x = util_rate * previous_state['V']
        x = previous_state['V'] * params['cyberlinks_util']
        if x > 7_000_000:
            x = 7_000_000
    else:
        x = 0
    return {'delta_CL': math.floor(x)}


def p_a(params, substep, state_history, previous_state):
    tokens = math.floor(previous_state['d_l'] / 2)
    d_a = math.floor((tokens / params['initPrice']) * (previous_state['maxVestingTime']/params['baseVestingTime']) * (previous_state['MRa'] / 100))
    return {'delta_a': math.floor(d_a)}


def p_v(params, substep, state_history, previous_state):
    tokens = math.floor(previous_state['d_l'] / 2)
    d_v = math.floor((tokens / params['initPrice']) * (previous_state['maxVestingTime']/params['baseVestingTime']) * (previous_state['MRv'] / 100))
    return {'delta_v': math.floor(d_v)}


def p_m_v_t(params, substep, state_history, previous_state):
    x = previous_state['timestep'] // params['unitsPerYear']
    d_m_v_t = params['baseVestingTime'] * (2**x)
    return {'delta_m_v_t': d_m_v_t}