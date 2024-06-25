user_preferences = {
    "timezone": "GMT",
    "language": "English",
    "notifications": None,
    "currency": "USD",
    "theme": None
}

def update_preferences(user_pref):
    new_user_preferences={}
    for key,value in user_preferences.items():
        if value != None:
            new_user_preferences[key]=value
    return new_user_preferences


print(update_preferences(user_preferences))
