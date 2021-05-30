def s_I_r(params, substep, state_history, previous_state, policy_input):
    I_r = previous_state['I_r'] + policy_input['IRC']
    if I_r > params['inflationMax']:
        I_r = params['inflationMax']
    elif I_r < params['inflationMin']:
        I_r = params['inflationMin']
    return 'I_r', I_r


def s_F(params, substep, state_history, previous_state, policy_input):
    F = previous_state['F'] + policy_input['delta_F']
    if F < 0:
        F = 0
    return 'F', F


def s_L(params, substep, state_history, previous_state, policy_input):
    L = previous_state['L'] + policy_input['delta_L'] - policy_input['delta_U']
    if L < 0:
        L = 0
    return 'L', L


def s_T(params, substep, state_history, previous_state, policy_input):
    T = previous_state['T'] - policy_input['delta_F'] - policy_input['delta_L'] + policy_input['provision'] + policy_input['delta_U']
    return 'T', T


def s_d_u(params, substep, state_history, previous_state, policy_input):
    return 'd_u', policy_input['delta_U']


def s_d_l(params, substep, state_history, previous_state, policy_input):
    return 'd_l', policy_input['delta_L']


def s_a(params, substep, state_history, previous_state, policy_input):
    a = previous_state['A'] + policy_input['delta_a']
    return 'A', a


def s_v(params, substep, state_history, previous_state, policy_input):
    v = previous_state['V'] + policy_input['delta_v']
    return 'V', v


def s_mr_a(params, substep, state_history, previous_state, policy_input):
    mr = policy_input['delta_MRa']
    if mr < 1:
        mr = 1
    return 'MRa', mr


def s_mr_v(params, substep, state_history, previous_state, policy_input):
    mr = policy_input['delta_MRv']
    if mr < 1:
        mr = 1
    return 'MRv', mr


def s_cl(params, substep, state_history, previous_state, policy_input):
    cl = previous_state['CL'] + policy_input['delta_CL']
    return 'CL', cl

def s_m_v_t(params, substep, state_history, previous_state, policy_input):
    m_v_t = policy_input['delta_m_v_t']
    return 'maxVestingTime', m_v_t