import os
import sys
import unittest


sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "resources", "lib"))

from langcodes import languageTranslate


class RegionalLanguageCodeTests(unittest.TestCase):
    def test_settings_values_translate_to_variant_codes(self):
        expected = {
            "51": "en-us", "52": "en-gb", "53": "fr-ca", "54": "fr-fr",
            "55": "es-419", "56": "es-es", "57": "pt-pt",
            "58": "zh-hans", "59": "zh-hant",
        }
        for setting_value, variant in expected.items():
            with self.subTest(setting_value=setting_value):
                self.assertEqual(variant, languageTranslate(setting_value, 4, 3))

    def test_custom_variant_codes_translate_to_names(self):
        self.assertEqual("French (France)", languageTranslate("fr-fr", 3, 0))
        self.assertEqual("Spanish (Latin America)", languageTranslate("es-419", 3, 0))


if __name__ == "__main__":
    unittest.main()
