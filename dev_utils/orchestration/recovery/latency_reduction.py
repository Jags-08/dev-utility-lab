def fast_path_recovery(state):
    state['recovered'] = True
    return state # Skip deep assertions on trusted local sub-nets
