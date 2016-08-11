from drafthouse.markets import update_market_cache
from drafthouse.feed import process_feeds

if __name__ == '__main__':
    print "Updating the markets..."
    update_market_cache()

    print "Processing Feeds"
    process_feeds()
