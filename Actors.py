#Import relevant modules
from neo4j.v1 import GraphDatabase, basic_auth

#Connect to the database. For security purposes the password here is anonymized (default pass). Please contact the author if you need additional details.
driver = GraphDatabase.driver("bolt://localhost:7687", auth=basic_auth("neo4j", "neo4j"))
#Open a session
session = driver.session()

#Run the filtering query in the session. Return all actors who have acted in movies where Keanu has. Do not list Keanu and return distinct results.  
result = session.run("MATCH (p:Actor)-[:ACTS_IN]-> (m) <-[:ACTS_IN]-(keanu)"
                     "WHERE NOT p.name = \"Keanu Reeves\""
                       "RETURN DISTINCT p.name AS name,m.title AS title")

#Print the result and close the session
for record in result:
    print("Movie: %s \n Name: %s \n" % (record["title"], record["name"]))

session.close()