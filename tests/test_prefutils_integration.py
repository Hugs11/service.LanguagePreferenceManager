import os
import sys
import types
import unittest


LIB_PATH = os.path.join(os.path.dirname(__file__), "..", "resources", "lib")
sys.path.insert(0, LIB_PATH)


xbmc = types.ModuleType("xbmc")
xbmc.Player = type("Player", (), {})
xbmc.Monitor = type("Monitor", (), {})
xbmc.sleep = lambda _milliseconds: None
sys.modules["xbmc"] = xbmc

xbmcaddon = types.ModuleType("xbmcaddon")
xbmcaddon.Addon = lambda: types.SimpleNamespace(getSetting=lambda _key: "")
sys.modules["xbmcaddon"] = xbmcaddon

xbmcvfs = types.ModuleType("xbmcvfs")
xbmcvfs.translatePath = lambda path: path
sys.modules["xbmcvfs"] = xbmcvfs

logger = types.ModuleType("logger")
logger.LOG_NONE, logger.LOG_INFO, logger.LOG_DEBUG, logger.LOG_ERROR = range(4)
logger.log = lambda *_args: None
sys.modules["logger"] = logger

custom_preferences = types.ModuleType("custom_media_preference")
custom_preferences.media_preference_manager = types.SimpleNamespace()
custom_preferences.CustomMediaPreference = type("CustomMediaPreference", (), {})
sys.modules["custom_media_preference"] = custom_preferences


class FakeSettings:
    subtitle_keyword_blacklist = []
    subtitle_keyword_blacklist_enabled = False
    audio_keyword_blacklist = []
    audio_keyword_blacklist_enabled = False
    ignore_signs_on = False


prefsettings = types.ModuleType("prefsettings")
prefsettings.settings = FakeSettings
sys.modules["prefsettings"] = prefsettings

from prefutils import LangPrefMan_Player


class PreferenceEvaluationTests(unittest.TestCase):
    def make_player(self):
        player = object.__new__(LangPrefMan_Player)
        player.selected_sub = {
            "index": 15, "language": "fre", "name": "Français (Canada)",
            "isforced": False,
        }
        player.subtitles = [
            player.selected_sub,
            {"index": 16, "language": "fre", "name": "Français (France)",
             "isforced": False},
        ]
        return player

    def test_subtitle_evaluator_selects_france_from_real_track_order(self):
        player = self.make_player()
        preferences = [(set(), [("French (France)", "fr-fr", "false")])]
        self.assertEqual(16, player.evalSubPrefs(preferences))

    def test_generic_french_preference_keeps_current_track(self):
        player = self.make_player()
        preferences = [(set(), [("French", "fre", "false")])]
        self.assertEqual(-1, player.evalSubPrefs(preferences))


if __name__ == "__main__":
    unittest.main()
