import thingspeak

channel_id = 236411
read_key    = EZAE6EWFSYVPG5LA


channel = thingspeak.Channel(id=channel_id,api_key=read_key)

# If you want text output instead of json try this
# channel = thingspeak.Channel(id=channel_id,api_key=api_key, fmt='txt')

try:
    # Get the last 2 results from field 1 of your channel
    print channel.get_field(field='field1', options = {'results': 2})
    # Get the age of the last data in field 1 of your channel in seconds
    print channel.get_last_data_age(field='field1')
    # Get the last data in field 1 of your channel
    print channel.get_field_last(field='field1')
except:
    raise
    print "connection failed"
