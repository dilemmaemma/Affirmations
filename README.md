# Affirmations
## Use
Backend program that users can utilize to either store affirmations to later pull them at any time, or get affirmations that have already been sent to the database. Affirmations can be searched based upon keywords or category

## Endpoints
`[GET] /affirmations/<category>` - Pulls all affirmations from a certain category
`[GET] /affirmations/<keyword>` - Pulls all affirmations with a certain keyword
`[GET] /affirmations/<category>/<keyword>` - Pulls all affirmations from a certain category that match a certain keyword
`[POST] /affirmations/<category>` - Adds user input affirmation to the SQL database
`[PATCH] /affirmations/<category>` - Edits user input affirmation and uploads it to the SQL database
`[DELETE] /affirmations/<category>` - Removes selected affirmation from database

## Packages Used
-To Be Updated-
