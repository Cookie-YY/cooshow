class DevDubug:
    def __init__(self):
        pass

    @staticmethod
    def get_specific_table(table, db="zb_db"):
        from utils.db_connection import fx_engine, zb_engine
        if db == "zb_db":
            engine = zb_engine
        else:
            engine = fx_engine
        try:
            db_results = engine.execute(f"select * from {table}")
        except:
            return 400, f"TableError: The table {[table]} does not in {db}", {}

        from utils.results2df import results2df
        db_results = results2df(db_results, db_results.keys())
        return 200, "success", db_results

