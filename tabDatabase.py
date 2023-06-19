from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, DateTime, ForeignKey, Float, Enum, \
    Index, text

DB_PATH = 'sqlite:////mnt/c/Users/yusuf/Documents/PG/tabData/tmp.sqlite'
tabEngine = create_engine(DB_PATH)
metadata = MetaData()

with tabEngine.connect() as c:
    c.execute(text('PRAGMA synchronous=OFF'))
    c.execute(text('PRAGMA journal_mode=MEMORY'))
    c.execute(text('PRAGMA cache_size=100000'))

tournament_table = Table(
    'tournament', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String, nullable=False),
    Column('webname', String),
    Column('country', String),
    Column('state', String),
    Column('city', String),
    Column('start', DateTime),
    Column('end', DateTime),
    Column('timezone', String)
)

category_table = Table(
    'category', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String, nullable=False),
    Column('abbr', String),
    Column('tournament', ForeignKey('tournament.id')),
)

event_table = Table(
    'event', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String),
    Column('abbr', String),
    Column('type', Enum('speech', 'congress', 'debate', 'wudc', 'wsdc', 'attendee')),
    Column('fee', Float),
    Column('category', ForeignKey('category.id'))
)

round_table = Table(
    'round', metadata,
    Column('id', Integer, primary_key=True),
    Column('type', String),
    Column('name', Integer),
    Column('start_time', DateTime),
    Column('protocol_name', String),
    Column('label', String),
    Column('flights', Integer),
    Column('runoff', ForeignKey('round.id')),
    Column('event', ForeignKey('event.id'))
)

section_table = Table(
    'section', metadata,
    Column('id', Integer, primary_key=True),
    Column('room', String),
    Column('letter', String),
    Column('bye', Integer),
    Column('flight', String),
    Column('round', ForeignKey('round.id'))
)

student_table = Table(
    'student', metadata,
    Column('id', Integer, primary_key=True),
    Column('first', String),
    Column('last', String)
)

# Replace null values with 0 so unique constraint works
team_unique = [text(f'coalesce({col}, 0)') for col in
               ('debater1', 'debater2', 'debater3', 'debater4', 'debater5', 'other_debaters')]
# Ids are in ascending order
team_table = Table(
    'team', metadata,
    Column('id', Integer, primary_key=True),
    Column('num_debaters', Integer),
    Column('debater1', ForeignKey('student.id'), index=True, nullable=False),
    Column('debater2', ForeignKey('student.id'), index=True, nullable=True),
    # A couple percent of entries have more than 2
    Column('debater3', ForeignKey('student.id'), nullable=True),
    Column('debater4', ForeignKey('student.id'), nullable=True),
    Column('debater5', ForeignKey('student.id'), nullable=True),
    # Like 10 entries have more than 5 (vs 2k with exactly 5) so just store those in comma seperated string
    Column('other_debaters', String, nullable=True),
    Index('ix_team_debaters', *team_unique, unique=True)
)

entry_table = Table(
    'entry', metadata,
    Column('id', Integer, primary_key=True),
    Column('code', String),
    Column('name', String),
    Column('short_name', String),
    Column('school_name', String),
    Column('school_code', String),
    Column('event', ForeignKey('event.id')),
    Column('team', ForeignKey('team.id'), index=True)
)

entry_student_table = Table(
    'entry_student', metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('entry', ForeignKey('entry.id'), index=True),
    Column('student', ForeignKey('student.id'), index=True),
    Index('ix_entry_student', 'entry', 'student', unique=True), extend_existing=True,
)

judge_table = Table(
    'judge', metadata,
    Column('id', Integer, primary_key=True),
    Column('code', String),
    Column('first', String),
    Column('last', String),
    Column('category', ForeignKey('category.id'))
)

ballot_table = Table(
    'ballot', metadata,
    Column('id', Integer, primary_key=True),
    Column('judge_started', DateTime),
    Column('side', Integer),
    Column('speakerorder', Integer),
    Column('chair', Integer),
    Column('bye', Integer),
    Column('forfeit', Integer),
    # _by fields are foreign key for something
    Column('entered_by', Integer),
    Column('started_by', Integer),
    Column('audited_by', Integer),
    Column('panel', Integer),  # Foreign key
    Column('judge', ForeignKey('judge.id')),
    Column('entry', ForeignKey('entry.id'), index=True),
    Column('section', ForeignKey('section.id'), index=True)
)

score_table = Table(
    'score', metadata,
    Column('id', Integer, primary_key=True),
    Column('tag', String),
    Column('value', Float),
    Column('speech', Integer),
    Column('speaker', ForeignKey('student.id')),
    Column('ballot', ForeignKey('ballot.id'))
)

result_set_table = Table(
    'result_set', metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('label', String),
    Column('bracket', Integer),
    Column('coach', Integer),
    Column('generated', DateTime),
    Column('event', ForeignKey('event.id')),
)

result_table = Table(
    'result', metadata,
    Column('id', Integer, primary_key=True),
    Column('rank', Integer),
    Column('place', String),
    Column('percentile', Float),
    Column('school', Integer),  # Foreign key for school
    Column('entry', ForeignKey('entry.id'), index=True),
    Column('student', ForeignKey('student.id')),
    Column('round', ForeignKey('round.id')),
    Column('result_set', ForeignKey('result_set.id')),
)

result_key_table = Table(
    'result_key', metadata,
    Column('id', Integer, primary_key=True),
    Column('tag', String),
    Column('description', String),
    Column('no_sort', Integer),
    Column('sort_desc', Integer),
    Column('result_set', ForeignKey('result_set.id'))
)

result_value_table = Table(
    'result_value', metadata,
    Column('id', Integer, primary_key=True),
    Column('value', String),
    Column('priority', Integer),
    Column('protocol', Integer),  # Foreign key
    Column('result_key', ForeignKey('result_key.id')),
    Column('result', ForeignKey('result.id'))
)
