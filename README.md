# Description

An Anki add-on that adds "Reset Limit Increases" to the bottom of each deck
overview screen, in order to reverse the effect of "Increase today's new card
limit" or "Increase today's review card limit" in Custom Study. Useful if
you've accidentally increased today's new card limit when you meant to raise
the review card limit.

NOTE: If you increase a limit on a subdeck of another deck, this will increase
the corresponding limit on the parent deck. After you reset limits on the
subdeck, the increased limit on the parent deck will still be in effect and not
reset, because there's no way to tell why a parent deck's limits were
increased - increasing the limits on either the parent deck or the subdeck will
lead to the same result. Resetting limits on a parent deck will reset limits on
the subdecks as well.

AnkiWeb: https://ankiweb.net/shared/info/738867649

# License

This addon is licensed under the same license as Anki itself (GNU Affero General
Public License 3).
