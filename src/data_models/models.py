from pydantic import BaseModel
from faker import Faker

faker = Faker()

class Generators:

    @staticmethod
    def rcpn_data():
        return [
            faker.first_name(),
            faker.last_name(),
            faker.postcode()
        ]

