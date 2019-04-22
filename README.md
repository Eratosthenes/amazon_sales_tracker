# Components
### Fetch and deposit
- Call amazon API for specified ASIN
- Pull Sales Rank, drop in database
- (# of reviews? If it can get the Audible review data?)
- Run once per hour for all tracked ASINs, forever.

### Database
- ASIN | Datetime | Amazon Sales Rank | Rating
- ASIN | Title | Product Type | JacobIsOwner(t/f) | Tracking(t/f)

### Add new ASINs to track
- Config file for ASINS

### Produce charts, statistics

#### Generate prebuilt reports:
- Line chart of past week, past month, year
- Table of current sales rankings of Jacob's items
