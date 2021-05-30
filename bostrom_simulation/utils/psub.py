from utils.policies import *
from utils.suf import *

partial_state_update_blocks = [
    {
        'policies': {
            'IRC': p_inflation,
            'provision': p_provision,
            'delta_F': p_claim,
            'delta_L': p_vest,
            'delta_U': p_unvest,
            'delta_MRa': p_mr_a,
            'delta_MRv': p_mr_v,
            'delta_CL': p_cl,
            'delta_a': p_a,
            'delta_v': p_v,
            'delta_m_v_t': p_m_v_t

        },
        'variables': {
            'I_r': s_I_r,
            'F': s_F,
            'L': s_L,
            'T': s_T,
            'd_u': s_d_u,
            'd_v': s_d_l,
            'A': s_a,
            'V': s_v,
            'MRa': s_mr_a,
            'MRv': s_mr_v,
            'CL': s_cl,
            'maxVestingTime': s_m_v_t
        }
    }
]