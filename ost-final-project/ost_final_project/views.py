from models import Resource, Reservation, Tag
import autheticate
import utility


class HomePageView(object):
    def __init__(self):
        # TODO(Ling): Build log_info.
        self.logged_in, self.user, self.log_url, self.log_msg = autheticate.autheticate()
        self.all_resources = self.get_all_resources()
        self.my_resources = self.get_my_resources()
        self.my_reservations = self.get_my_reservations()

    def get_all_resources(self):
        # TODO(Ling): Implement multiple pages.
        data = Resource.query().fetch(20)
        return data

    def get_my_resources(self):
        # TODO(Ling): Implement multiple pages.
        data = Resource.query(Resource.owner == self.user).fetch(20)
        return data

    def get_my_reservations(self):
        # TODO(Ling): Implement multiple pages.
        models = Reservation.query().fetch(20)
        data = []
        for reservation in models:
            data.append(ReservationView(reservation))
        return data


class CreateResourceView(object):
    def __init__(self):
        # TODO(Ling): Build log_info.
        self.logged_in, self.user, self.log_url, self.log_msg = autheticate.autheticate()


class CreateReservationView(object):
    def __init__(self, resource_id):
        # TODO(Ling): Build log_info.
        self.logged_in, self.user, self.log_url, self.log_msg = autheticate.autheticate()
        self.resource_id = resource_id
        self.resource = utility.get_resource_by_id(self.resource_id)


class ResourceView(object):
    def __init__(self, resource_id):
        self.resource_id = resource_id
        self.resource = utility.get_resource_by_id(self.resource_id)


class ReservationView(object):
    def __init__(self, reservation):
        self.model = reservation
        self.key = reservation.key
        self.owner = reservation.owner
        self.start_time = reservation.start_time
        self.end_time = reservation.end_time
        self.resource = self.get_resource()

    # TODO(Ling): Get the entity by key.
    def get_resource(self):
        return utility.get_resource_by_id(self.model.resource_key.id())