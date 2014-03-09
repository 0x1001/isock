import unittest
import isock

class _echo(isock.Action):
    def action(self,data):
        return data

class _serverVar(isock.Action):
    def __init__(self,server_variable):
        self.server_variable = server_variable

    def action(self,data):
        return self.server_variable

class IsockBasicTest(unittest.TestCase):
    def setUp(self):
        import threading

        try: self.server = isock.Server("localhost",4444)
        except isock.ServerException as error: self.fail("Init Error" + str(error))

        self.server.registerAction(_echo())

        server_variable = "dummy"
        self.server.registerAction(_serverVar(server_variable))

        threading.Thread(target=self.server.serve_forever).start()

    def tearDown(self):
        self.server.shutdown()

    def test_isockBasic(self):
        client = isock.Client("localhost",4444)
        data_to_send = "dummy"
        received_data = client.executeAction(_echo,data_to_send)
        self.assertEqual(data_to_send,received_data)

        received_data = client.executeAction(_serverVar)
        self.assertEqual("dummy",received_data)

if __name__ == '__main__':
    unittest.main()