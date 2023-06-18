"""SUDO CODE
def minimax(state, player):
    # given a state s:
        # MAX picks a in Actions(s) that produces highest val on MIN-Val(Result(s, a))
        
        # MIN pick a in Actions(s) that produces smallest value of MAX-Val(Result(s, a))
    pass


def max_Value(state):
    if terminal(state):
        return utility(state)
    
    v = - infinity
    
    for action in Actions(state):
        v = max(v, minValue(result(state, action)))
    
    return 


def min_Value(state):
    if terminal(state):
        return utility(state)
    
    v = infinity
    
    for action in Actions(state):
        v = min(v, minValue(result(state, action)))

"""