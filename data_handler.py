import json

class Data:
    def __init__(self):
        with open('data.json', 'r', encoding='utf8') as data_file:
            self.data = json.load(data_file)

    def get_tours(self, departure):
        filtered_tours = []
        for tour in self.data['tours']:
            if tour['departure'] == departure:
                filtered_tours.append(tour)
        return filtered_tours

    def get_departure(self, departure):
        tour_departure = self.data['departures']
        return tour_departure[departure]

    def get_tour_prices(self, departure):
        tours = self.get_tours(departure)
        tour_prices = []
        for tour in tours:
            tour_prices.append(tour['price'])
        return tour_prices

    def get_tour_price(self, id):
        tour = self.data['tours']
        tour_price = tour[id-1]['price']
        return tour_price 
        
    def get_tours_duration_of_stay(self, departure):
        tours = self.get_tours(departure)
        tours_duration_of_stay = []
        for tour in tours:
            tours_duration_of_stay.append(tour['nights'])
        return tours_duration_of_stay

    def get_tour_duration_of_stay(self, id):
        tour = self.data['tours']
        tour_duration_of_stay = tour[id-1]['nights']
        return tour_duration_of_stay

    def get_tour_picture(self, id):
        tour = self.data['tours']
        tour_picture = tour[id-1]['picture']
        return tour_picture

    def get_tour_content(self, id):
        tour = self.data['tours']
        tour_content = tour[id-1]['description']
        return tour_content
