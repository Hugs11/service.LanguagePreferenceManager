service.LanguagePreferenceManager
=================================

[![Build Kodi add-on](https://github.com/Hugs11/service.LanguagePreferenceManager/actions/workflows/build.yml/badge.svg)](https://github.com/Hugs11/service.LanguagePreferenceManager/actions/workflows/build.yml)

A manager for audio and subtitle preferences
============================================

This addon provides an easy way to set your preferred audio streams and subtitle languages in Kodi.

This is a small community fork of
[rockrider69/service.LanguagePreferenceManager](https://github.com/rockrider69/service.LanguagePreferenceManager),
focused on distinguishing regional and script variants that share the same
legacy ISO 639 language code in Kodi.

Regional and script variants are supported for languages commonly found more
than once in the same media file: English (United States/United Kingdom), French
(Canada/France), Spanish (Latin America/Spain), Portuguese (Brazil/Portugal),
and Chinese (Simplified/Traditional). The add-on first uses a BCP-47 language
tag when Kodi exposes one, then recognizes common labels in the track name.
A generic language preference remains compatible with every one of its
variants.

For custom preferences, use `en-us`, `en-gb`, `fr-ca`, `fr-fr`, `es-419`,
`es-es`, `pt-br`, `pt-pt`, `zh-hans`, or `zh-hant`. A regional preference
selects an exact variant first, then an unlabelled track of the same language;
it does not silently select a track explicitly labelled as another region.

Installable ZIP files are available from the
[latest release](https://github.com/Hugs11/service.LanguagePreferenceManager/releases/latest).
GitHub Actions also runs the tests and builds a temporary artifact on every
push.

You can select which audio tracks and subtitles to automatically activate based on your priorities, and define simple conditional rules like "if audio is xxx then activate subtitles yyy" via drop/down lists.
More advanced custom rules can be defined as well (see changelog for more on the syntax. Note that custom rules always take precedence over others).

Special language codes None(non) for subtitles and Any(any) for audio can be used in Conditional Subtitles Rules, normal or custom.
For example "fre:non>any:fre>any:eng" will disable subtitles if audio is French (except if a french forced subtitles track exists) and activate french subtitles for any other audio language. If these are not available it will try the same finding english subtitles.

Rules are re-evaluated and applied whenever you switch audio while watching (from v0.1.5).

It's now also possible to force ignore "Signs and Songs" subtitles in preferences evaluations, based on name, and/or any other subtitle tracks based on predefined keywords.
For example, most dual audio Anime provides english and japanese audio and two english subtitles. Dialogue subtitles with all the dialogue to go with the japanese audio and Song/Sign subtitles which only translate song lyrics and signs you see on screen to be used with the english audio stream. Previously the addon just picked the first subtitles with the correct language which weren't always the correct ones.

An option allows you to store forced preferences per Movie / TVshow (from v1.0.6). When you manually change audio and/or subtitle tracks during play, this will be saved as an overriding preference, taking precedence over all other rules for the next opening of the Movie, or the next episode of the TVshow (Thx a lot to SgtJalau!)

Special Thanks
==============

- @ace20022 and @scott967 for initial development

- @cyberden for making this addon ready for Kodi Matrix

- @fpatrick for fixing an issue with language mapping

- @KnappeGEIL for ideas how to ignore 'Signs and Songs' subtitles

- @SgtJalau for the complete feature to store specific/overriding preferences per Movie / TVshow
