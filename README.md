# Affirmations
## Use
Backend program that users can utilize to either store affirmations to later pull them at any time, or get affirmations that have already been sent to the database. Affirmations can be searched based upon keywords or category

## Endpoints
### Private
- `[GET] /affirmations` - Pulls all affirmations from database
- `[GET] /affirmations/<int:affirmation_id>` - Pulls affirmation with specific id
- `[GET] /affirmations/category:<category>` - Pulls all affirmations from a certain category
- `[GET] /affirmations/keyword:<keyword>` - Pulls all affirmations with a certain keyword
- `[GET] /affirmations/category:<category>/keyword:<keyword>` - Pulls all affirmations from a certain category that match a certain keyword
- `[POST] /affirmations` - Adds affirmation to the SQL database
- `[PATCH] /affirmations/<int:affirmation_id>` - Edits affirmation and uploads it to the SQL database
- `[DELETE] /affirmations/<int:affirmation_id>` - Removes selected affirmation from database
### Public
- `[GET] /affirmations/public` - Pulls all public affirmations
- `[GET] /affirmations/public/<int:affirmation_id>` - Pulls public affirmation with specific id
- `[GET] /affirmations/public/category:<category>` - Pulls all public affirmations from a certain category
- `[GET] /affirmations/public/keyword:<keyword>` - Pulls all public affirmations with a certain keyword
- `[GET] /affirmations/public/category:<category>/keyword:<keyword>` - Pulls all public affirmations from a certain category that match a certain keyword

## Packages Used
- Flask
    - Creator: Armin Ronacher
    - <a href='https://github.com/pallets/flask'>Link</a>
- Flask-Mongoengine
    - Creator: Ross Lawley
    - <a href='https://github.com/MongoEngine/flask-mongoengine'>Link</a>
- Flask-SQLAlchemy
    - Creator: Armin Ronacher
    - <a href='https://github.com/pallets-eco/flask-sqlalchemy'>Link</a>
- Mongoengine
    - Creator: Harry Marr
    - <a href='https://github.com/MongoEngine/mongoengine'>Link</a>
- SQLAlchemy
    - Creator: Michael Bayer
    - <a href='https://github.com/sqlalchemy/sqlalchemy'>Link</a>
