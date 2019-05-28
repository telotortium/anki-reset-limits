# -*- coding: utf-8 -*-
# See github page to report issues or to contribute:
# https://github.com/telotortium/anki-reset-limits
#
# Contributors:
# - @telotortium
#
# Based on https://github.com/Arthaey/anki-rebuild-all.

from anki.hooks import wrap
from aqt.overview import Overview
from aqt.utils import shortcut, tooltip


def _handleResetLimitsButton(self, url):
    if url != "resetLimits":
        return False
    dconf = self.mw.col.decks.confForDid(self.mw.col.decks.selected())
    newDefaultLimit = dconf['new']['perDay']
    revDefaultLimit = dconf['rev']['perDay']
    currentDeck = self.mw.col.decks.current()
    newToday = currentDeck['newToday']
    revToday = currentDeck['revToday']
    newToday[1] = 0
    revToday[1] = 0
    self.mw.col.decks.current().update({
        'newToday': newToday,
        'revToday': revToday,
    })
    self.mw.col.decks.save()
    self.mw.col.decks.flush()
    tooltip("Reset today's new and review limits")
    self.mw.reset()


def _renderBottom(self):
    """Override Overview._renderBottom in order to add Reset Limits button.

    TODO: there seems to be no clean way to add a button. I've resorted to
    copying the body of Overview._renderBottom and adding the link here.
    Hopefully we can find a better way to do this in the future.
    """
    links = [
        ["O", "opts", _("Options")],
    ]
    if self.mw.col.decks.current()['dyn']:
        links.append(["R", "refresh", _("Rebuild")])
        links.append(["E", "empty", _("Empty")])
    else:
        links.append(["C", "studymore", _("Custom Study")])
        #links.append(["F", "cram", _("Filter/Cram")])
    if self.mw.col.sched.haveBuried():
        links.append(["U", "unbury", _("Unbury")])
    links.append(["L", "resetLimits", _("Reset Limit Increases")])
    buf = ""
    for b in links:
        if b[0]:
            b[0] = _("Shortcut key: %s") % shortcut(b[0])
        buf += """
<button title="%s" onclick='pycmd("%s")'>%s</button>""" % tuple(b)
    self.bottom.draw(buf)
    self.bottom.web.onBridgeCmd = self._linkHandler


Overview._renderBottom = wrap(Overview._renderBottom, _renderBottom, "after")
Overview._linkHandler = wrap(Overview._linkHandler, _handleResetLimitsButton, "after")
