class Street:
    def __init__(self, intersection_start, intersection_end, street_name, travel_duration_in_sec):
        self.intersection_start = intersection_start
        self.intersection_end = intersection_end
        self.street_name = street_name
        self.travel_duration_in_sec = travel_duration_in_sec

    # Custom print
    def __str__(self):
        return str(self.__class__) + ';Starting Intersection: ' + str(self.intersection_start) + ';Ending Intersection: ' +  str(self.intersection_end) + ';Street Name: ' +  str(self.street_name) + ';Travel Duration In Sec: ' +  str(self.travel_duration_in_sec)
