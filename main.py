import requests
import pprint


class BaseRequest:
    def __init__(self, base_url):
        self.base_url = base_url

    def _request(self, url, request_type, data=None, expected_error=False):
        stop_flag = False
        while not stop_flag:
            if request_type == 'GET':
                response = requests.get(url)
            elif request_type == 'POST':
                response = requests.post(url, data=data)
            elif request_type == 'PUT':
                response = requests.put(url, data=data)
            else:
                response = requests.delete(url)

            if not expected_error and response.status_code == 200:
                stop_flag = True
            elif expected_error:
                stop_flag = True

        pprint.pprint(f'{request_type} example')
        pprint.pprint(response.url)
        pprint.pprint(response.status_code)
        pprint.pprint(response.reason)
        pprint.pprint(response.text)
        pprint.pprint(response.json())
        pprint.pprint('**********')
        return response

    def get(self, endpoint, endpoint_id, expected_error=False):
        url = f'{self.base_url}/{endpoint}/{endpoint_id}'
        response = self._request(url, 'GET', expected_error=expected_error)
        return response.json()

    def post(self, endpoint, endpoint_id, body):
        url = f'{self.base_url}/{endpoint}/{endpoint_id}'
        response = self._request(url, 'POST', data=body)
        return response.json()['message']

    def delete(self, endpoint, endpoint_id):
        url = f'{self.base_url}/{endpoint}/{endpoint_id}'
        response = self._request(url, 'DELETE')
        return response.json()['message']

    def put(self, endpoint, endpoint_id, body):
        url = f'{self.base_url}/{endpoint}/{endpoint_id}'
        response = self._request(url, 'PUT', data=body)
        return response.json()['message']


BASE_URL = 'https://jsonplaceholder.typicode.com'

base_request = BaseRequest(BASE_URL)


user_info = base_request.get('users', 1)
pprint.pprint(user_info)


data = {
    'name': 'Test_USER1',
    'username': 'user1_test',
    'email': 'user1@mail.com'
}
new_user = base_request.post('users', 1, data)
pprint.pprint(new_user)


updated_data = {
    'name': 'admin_USER',
    'username': 'admin',
    'email': 'admin@gmail.com'
}
updated_user = base_request.put('users', 1, data= updated_data)
pprint.pprint(updated_user)


deleted_user = base_request.delete('users', 1)
pprint.pprint(deleted_user)

BASE_URL = 'https://petstore.swagger.io/v2'
base_request = BaseRequest(BASE_URL)


inventory = base_request.get('store', 'inventory')
pprint.pprint(inventory)


order_data = {

    'id': 3,
    'petId': 3,
    'quantity': 2,
    'shipDate': '2025-11-07T10:00:00.000Z',
    'status': 'APPROVED',
    'complete': True
}

new_order = base_request.post('store', 'order', data= order_data)
pprint.pprint(new_order)


updated_order_data = {

    'id': 2,
    'petId': 1,
    'quantity': 4,
    'shipDate': '2026-10-08T10:00:00.000Z',
    'status': 'APPROVED',
    'complete': False
}

updated_order = base_request.put('store', 'order/3', data= updated_order_data)
pprint.pprint(updated_order)


deleted_order = base_request.delete('store', 'order/2')
pprint.pprint(deleted_order)
