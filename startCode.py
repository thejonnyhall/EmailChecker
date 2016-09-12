# Python lols
# Only-Code-In-Kebab-Case

from linkedin import linkedin
from oauthlib import *

# Adam's Emails
# hibblea@qut.edu.au
# adam.hibble@connect.qut.edu.au

consumer-key = '75kkkkhud4u9fj'
consumer-secret = '68qABdIFaAXYRYLS'
return-url = 'http://localhost:8080'


authentication = linkedin.LinkedInAuthentication(Consumer-key, consumer-secret, return-url, linkedin.PERMISSIONS.enums.values())

print authentication.authorization_url  # open this url on your browser
application = linkedin.LinkedInApplication(authentication)
