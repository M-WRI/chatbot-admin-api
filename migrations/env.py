from logging.config import fileConfig
import os
from dotenv import load_dotenv
from sqlalchemy import engine_from_config, pool, MetaData
from alembic import context
from app.modules.users.models import User
from app.modules.chatbots.models import Chatbot, Session, Interaction

load_dotenv()

config = context.config

database_url = os.getenv("DATABASE_URL")

if not database_url:
    raise ValueError("DATABASE_URL is not set in the environment variables.")

config.set_main_option("sqlalchemy.url", database_url)

if config.config_file_name is not None:
    fileConfig(config.config_file_name)

metadata = MetaData()

for model in [User, Chatbot, Session, Interaction]:
    for table in model.metadata.tables.values():
        table.tometadata(metadata)

target_metadata = metadata

def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online() -> None:
    """Run migrations in 'online' mode."""
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()