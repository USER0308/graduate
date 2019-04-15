# encoding: utf-8
import unittest


class SoftwareDownloadTest(unittest.TestCase):
    def tearDown(self):
        # 每个测试用例之后执行的操作
        pass

    def setUp(self):
        # 每个测试用例之前执行的操作
        pass

    @classmethod
    def tearDownClass(self):
        # 所有测试运行完后执行一次
        pass

    @classmethod
    def setUpClass(self):
        # 所有测试运行前执行一次
        pass

    def test_curl_install_run(self):
        pass

    def test_pip_install_run(self):
        pass

    def test_docker_install_run(self):
        pass

    def test_docker_compose_install_run(self):
        pass

    def test_image_download_run(self):
        pass

    def test_binary_download_run(self):
        pass

if __name__ == '__main__':
    unittest.main()