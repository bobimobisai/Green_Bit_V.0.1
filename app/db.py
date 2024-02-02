from config import db_user, db_pass
from psycopg_pool import AsyncConnectionPool
from psycopg_pool import errors

db_conf = f"dbname=admin user={db_user} password={db_pass} host=127.0.0.1 port=5432"

pool = AsyncConnectionPool(conninfo=db_conf, open=False)


async def open_pool():
    await pool.open()
    await pool.wait()
    print("Connection Pool Opened")


async def select_fetchall(query, args):
    async with pool.connection() as conn:
        async with conn.cursor() as cursor:
            await cursor.execute(query, args)
            results = await cursor.fetchall()
            return results


async def write(query, args):
    async with pool.connection() as conn:
        async with conn.cursor() as cursor:
            await cursor.execute(query, args)
            if "RETURNING" in query:
                results = await cursor.fetchone()
                return results
            else:
                await conn.commit()
                return


# CRUD


async def create_data(data):
    try:
        query_1 = """
        INSERT INTO "user" (user_id)
        VALUES (%s);
        """
        result = await write(query=query_1, args=data)
        return result
    except errors as e:
        print(e)
        return {"ERROR": e}


async def read_data(args):
    try:
        query_1 = """
        SELECT * FROM "user" WHERE user_id = %s;
        """
        result = await select_fetchall(query=query_1, args=args)
        return result
    except errors as e:
        print(f"Error in create function: {e}")
        return {"ERROR": e}


async def update_data(data, args, column):
    try:
        query_1 = f"""
        UPDATE "user"
        SET {column} = {data}
        WHERE user_id = %s
        """
        result = await write(query=query_1, args=args)
        return result
    except errors as e:
        print(f"Error in create function: {e}")
        return {"ERROR": e}


async def delete_data(args):
    try:
        query_1 = """
        DELETE FROM "user"
        WHERE user_id = %s
        """
        await write(query=query_1, args=args)
    except errors as e:
        print(f"Error in delete_user function: {e}")
        return {"ERROR": e}
