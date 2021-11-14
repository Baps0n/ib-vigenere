import unittest
import main


class VigenereTest(unittest.TestCase):
    def test_EBK(self):
        self.assertEqual(main.encode_by_key("practice_ib_test", "key"), "zvymxgmi_gl_xccx")

    def test_DBK(self):
        self.assertEqual(main.decode_by_key("zvymxgmi_gl_xccx", "key"), "practice_ib_test")

    def test_EBM(self):
        self.assertEqual(main.encode_by_msg("practice_ib_test", "k"), "zgrcvbkg_mj_uxwl")

    def test_DBM(self):
        self.assertEqual(main.decode_by_msg("zgrcvbkg_mj_uxwl", "k"), "practice_ib_test")

    def test_EBEM(self):
        self.assertEqual(main.encode_by_enc_msg("practice_ib_test", "k"), "zqqsltvz_hi_bfxq")

    def test_DBEM(self):
        self.assertEqual(main.decode_by_enc_msg("zqqsltvz_hi_bfxq", "k"), "practice_ib_test")


if __name__ == "__main__":
    unittest.main()
