User Story
----------
| As a Developer of current project
| I want to see the last commit
| That I could see current changes at the project


Acceptance criteria
-------------------
**Scenario** - Last commit

| *Given* - https://github.com/django/django/commits/master with commits and https://github.com/django/django with commit in header
| *When* - comparing last commit on https://github.com/django/django/commits/master with commit in header on https://github.com/django/django
| *Then* - on https://github.com/django/django is displayed last commit
