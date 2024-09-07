referrals = {'alex': ['john', 'ridho'],
            'ridho': ['obi', 'ali'],
            'vio': ['john', 'ali'],
            'ali': ['heru'],
             'john':[],
             'obi':[]
}

def get_total_rewards(name):
    first_tiers = referrals[name]
    c_first_tiers = len(first_tiers)
    total_rewards = c_first_tiers * 5
    
    
    for first_tier in first_tiers:
        second_tiers = referrals[first_tier]
        c_second_tiers = len(second_tiers)

        total_rewards += (c_second_tiers * 3)
    
    return total_rewards


