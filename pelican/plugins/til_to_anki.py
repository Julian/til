"""
Output each article into an Anki deck.
"""

from pelican import signals
import attr
import genanki


# Hard coded random IDs hooray
DECK_ID = 2496816039
MODEL_ID = 1410818441

HOORAY_GLOBAL_STATE = []


til = genanki.Model(
    MODEL_ID,
    "TIL",
    fields=[{"name": "Title"}, {"name": "Contents"}],
    templates=[
        dict(
            name="Card 1",
            qfmt="{{Title}}",
            afmt='{{FrontSide}}<hr id="contents">{{Contents}}',
        ),
    ],
)


@attr.s
class AnkiPelicanWriter:

    _deck = attr.ib()

    def _add_article(self, _, content):
        note = genanki.Note(
            model=til,
            fields=[content.title, content.content],
        )
        self._deck.add_note(note)

    def _write_deck(self, pelican):
        genanki.Package(self._deck).write_to_file("til.apkg")

        assert HOORAY_GLOBAL_STATE, HOORAY_GLOBAL_STATE
        HOORAY_GLOBAL_STATE.clear()


    @classmethod
    def connected(cls, pelican):
        if not pelican.settings.get("ANKITIL"):
            return
        name = pelican.settings["SITENAME"]
        deck = genanki.Deck(deck_id=DECK_ID, name=name)
        writer = cls(deck=deck)

        assert not HOORAY_GLOBAL_STATE, HOORAY_GLOBAL_STATE
        HOORAY_GLOBAL_STATE.append(writer)

        signals.article_generator_write_article.connect(writer._add_article)
        signals.finalized.connect(writer._write_deck)


def register():
    signals.initialized.connect(AnkiPelicanWriter.connected)
