
HOST_IP = '127.0.0.1'
USER_PORT = '5003'
ORDER_PORT = '5004'
GATEWAY_PORT = '5005'

USER_SERVICE_URL = 'http://'+HOST_IP+':'+USER_PORT+'/users/'
ORDER_SERVICE_URL = 'http://'+HOST_IP+':'+ORDER_PORT+'/orders/'

CODE_SUCCESS = 200
CODE_NOT_FOUND = 404

USER_DETAIL = {
        1: {'name': 'Ganesha S', 'age': 34},
        2: {'name': 'Veeresh', 'age': 32}
    }

ORDER_DETAIL = {
       101: {'prodcut': 'Laptop HP Elitebook', 'price': 95450},
       102: {'prodcut': 'Mobile Vivo X60', 'price': 35000}
    }