from typing import Optional
import psycopg2

def constr(
        host: str,
        port: int,
        user: str,
        password: Optional[str],
        dbname: str):
    cs = (
            f"host={host} "
            f"port={port} "
            f"user={user} "
            f"password={password} "
            f"dbname={dbname} "
        )
    if password:
        cs += f"password={password} "

    return cs

def connect(host, port, user, password, dbname):
    return psycopg2.connect(constr(host,port,user,password,dbname))
