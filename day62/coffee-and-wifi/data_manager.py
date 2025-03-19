import pandas, os

class DataManager:
    ...

def get_csv_data():
    print(os.getcwd())
    data = pandas.read_csv("cafe-data.csv")
    return data

def set_data_to_csv(form):
    cafe_name = form.cafe_name.data
    cafe_location = form.cafe_location.data
    open_time = form.open_time.data
    close_time = form.close_time.data
    coffee_rating = form.coffee_rating.data
    wifi_rating = form.wifi_rating.data
    power_socket = form.power_socket.data
    data_dict = {
        'cafe_name': cafe_name,
        'cafe_location': cafe_location,
        'open_time': open_time,
        'close_time': close_time,
        'coffee_rating': coffee_rating,
        'wifi_rating': wifi_rating,
        'power_socket': power_socket,
    }
    data_frame = pandas.DataFrame(data_dict, index=[0])
    data_frame.to_csv("cafe-data.csv", mode='a', index=False, header=False)