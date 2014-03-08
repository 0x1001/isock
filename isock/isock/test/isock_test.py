import unittest
import isock

class _echo(isock.Action):
    def action(self,data):
        return data

class IsockBasicTest(unittest.TestCase):
    def setUp(self):
        import threading

        try: self.server = isock.Server("localhost","4444")
        except isock.ServerException as error: self.fail("Init Error" + str(error))

        self.server.registerAction(_echo())

        threading.thread(target=self.server.serve_forever).start()

    def tearDown(self):
        self.server.shutdown()

    def test_isockEcho(self):
        client = isock.Client()
        data_to_send = "dummy"
        received_data = client.executeAction(_echo,data_to_send)
        self.assertEqual(data_to_send,received_data)

if __name__ == '__main__':
    unittest.main()