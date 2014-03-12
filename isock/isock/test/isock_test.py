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

class _notAction(object): pass

class IsockBasicTest(unittest.TestCase):
    def setUp(self):
        import threading

        try: self.server = isock.Server("localhost",4440)
        except isock.ServerException as error: self.fail("Init Error" + str(error))

        self.server.addAction(_echo())

        server_variable = "dummy"
        self.server.addAction(_serverVar(server_variable))

        self.thread = threading.Thread(target=self.server.serve_forever)
        self.thread.start()

    def tearDown(self):
        self.server.shutdown()
        self.server.server_close()
        self.thread.join()

    def test_isockBasic(self):
        client = isock.Client("localhost",4440)
        data_to_send = "dummy"
        received_data = client.runAction(_echo,data_to_send)
        self.assertEqual(data_to_send,received_data)

        received_data = client.runAction(_serverVar)
        self.assertEqual("dummy",received_data)

class ISockServerExceptionTeste(unittest.TestCase):
    def test_exceptionAction(self):
        import threading
        server = isock.Server("localhost",4441)
        server.addAction(_echo())

        with self.assertRaises(isock.ServerException):
            server.addAction(_echo())

        with self.assertRaises(isock.ServerException):
            server.addAction(_notAction())

        thread = threading.Thread(target=server.serve_forever)
        thread.start()

        server.shutdown()
        server.server_close()

class ISockPortTaken(unittest.TestCase):
    def test_exceptionPortTaken(self):
        import threading
        server = isock.Server("localhost",4442)

        with self.assertRaises(isock.ServerException):
            server2 = isock.Server("localhost",4442)

        thread = threading.Thread(target=server.serve_forever)
        thread.start()
        server.shutdown()
        server.server_close()

class ISockClientExceptionTest(unittest.TestCase):
    def setUp(self):
        import threading

        try: self.server = isock.Server("localhost",4443)
        except isock.ServerException as error: self.fail("Init Error" + str(error))

        self.thread = threading.Thread(target=self.server.serve_forever)
        self.thread.start()

    def tearDown(self):
        self.server.shutdown()
        self.server.server_close()
        self.thread.join()

    def test_isockBasic(self):
        client = isock.Client("localhost",4443)

        with self.assertRaises(isock.ServerException):
            received_data = client.runAction(_echo)

class ISockClientRetryTest(unittest.TestCase):
    def test_retry(self):
        client = isock.Client("localhost",4444)

        with self.assertRaises(isock.ClientException):
            received_data = client.runAction(_echo)

class IsockActionTest(unittest.TestCase):
    def setUp(self):
        import threading

        try: self.server = isock.Server("localhost",4445)
        except isock.ServerException as error: self.fail("Init Error" + str(error))

        self.thread = threading.Thread(target=self.server.serve_forever)
        self.thread.start()

    def tearDown(self):
        self.server.shutdown()
        self.server.server_close()
        self.thread.join()

    def test_actionTest(self):
        client = isock.Client("localhost",4445)

        data_to_send = "dummy"

        with self.assertRaises(isock.ServerException):
            received_data = client.runAction(_echo,data_to_send)

        self.server.addAction(_echo())

        received_data = client.runAction(_echo,data_to_send)
        self.assertEqual(data_to_send,received_data)

class IsockClientActionException(unittest.TestCase):
    def setUp(self):
        import threading

        try: self.server = isock.Server("localhost",4445)
        except isock.ServerException as error: self.fail("Init Error" + str(error))

        self.thread = threading.Thread(target=self.server.serve_forever)
        self.thread.start()

    def tearDown(self):
        self.server.shutdown()
        self.server.server_close()
        self.thread.join()

    def test_clientActionTest(self):
        client = isock.Client("localhost",4445)

        data_to_send = "dummy"

        with self.assertRaises(isock.ClientException):
            received_data = client.runAction(_echo(),data_to_send)

        with self.assertRaises(isock.ClientException):
            received_data = client.runAction(None,data_to_send)


if __name__ == '__main__':
    unittest.main()