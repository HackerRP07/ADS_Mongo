from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider


contact_points = ['127.0.0.1']  # Replace with the actual contact points
auth_provider = PlainTextAuthProvider(username='Ritesh', password='123456')  # Replace with actual credentials if needed

cluster = Cluster(contact_points=contact_points, auth_provider=auth_provider)
session = cluster.connect()

session.set_keyspace('first')

query = "SELECT * FROM person"
result = session.execute(query)
for row in result:
    print(row)