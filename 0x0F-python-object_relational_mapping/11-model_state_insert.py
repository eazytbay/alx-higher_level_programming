#!/usr/bin/python3
'''
script that adds the State object “Louisiana” to the database hbtn_0e_6_usa
'''

if __name__ == '__main__':
    import sys
    from model_state import State, Base
    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session

    datab_engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(datab_engine)

    session = Session(datab_engine)
    fr_state = 'Louisiana'
    inc_state = State(name=fr_state)
    session.add(inc_state)

    fr_state_record = session.query(State).filter(
        State.name == fr_state).first()

    session.commit()

    print('{}'.format(fr_state_record.id))

    session.close()
