from fastapi import HTTPException

from common.utils import postgres


def get_by_state(state, nb_per_page, page_nb):
    """
    Get covid by State

    Parameters
    ----------
    state : str : US State
    nb_per_page : int : number of item per page
    page_nb : int : page number

    Example
    -------
    covid = get_by_state(state, nb_per_page, page_nb)
    """
    if nb_per_page > 100:
        raise HTTPException(status_code = 401, detail = "covid offset invalid - set lower value")

    conn = postgres.get_pg_client()

    sql = '''
        SELECT
            date,
            cases,
            deaths,
            states.name AS states,
            counties.name AS counties,
            counties.fips AS fips
        FROM covid
        JOIN states ON covid.state_id = states.id
        JOIN counties ON covid.county_id = counties.id
        WHERE states.name = %s
        ORDER BY covid.id OFFSET %s ROWS FETCH NEXT %s ROWS ONLY;
    '''

    offset = ((page_nb - 1) * nb_per_page)

    covid_data = conn.execute(sql, (state, offset, nb_per_page))
    covid_data_dict = covid_data.mappings().all()

    return covid_data_dict
