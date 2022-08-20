import cx_Oracle

# Connect as user "hr" with password "welcome" to the "orclpdb1" service running on this computer.
uid = "TVCORP"
pwd = "Xbc893nf9nd"
db = "ORACLE10G:1521:ADAMI"
connection = cx_Oracle.connect(uid+"/"+pwd+"@"+db)

cursor = connection.cursor()
cursor.execute("""
        select '' nada,\"Placa\" from coadami.VW_CaminhoesConferencia""",
        did = 50,
        eid = 190)
for fname, lname in cursor:
    print("Values:", fname, lname)