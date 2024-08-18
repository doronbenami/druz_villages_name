def update_city_name(prefix, city_name):
    first_digit = str(prefix)[0]
    if first_digit == '1':
        return 'כסרא'
    elif first_digit == '2':
        return 'סמיע'
    elif first_digit == '3':
        return 'בית גן'
    elif first_digit == '4':
        return 'חורפיש'
    elif first_digit == '5':
        return 'ריחאניה'
    elif first_digit == '6':
        return 'פקיעין'
    elif first_digit == '7':
        return 'גת'
    elif first_digit == '8':
        return 'ינוח'
    else:
        return 'NO'  # Keep the original name if prefix does not match

# Call the function with your columns
update_city_name(!prefix_column!, !city_name_column!)
