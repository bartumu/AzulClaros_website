import os
import shutil
import django
from django.conf import settings
from django.core.cache import cache
from django.core.management import call_command

def setup_django():
    """Configura o Django para usar as configurações do projeto."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'AzulClaros.settings')
    django.setup()

def clear_cache():
    """Limpa o cache do Django."""
    cache.clear()
    print("Cache limpo.")

def remove_migrations():
    """Remove todos os arquivos de migrações."""
    for root, dirs, files in os.walk('.'):
        for file in files:
            if file != "__init__.py" and file.endswith(".py"):
                if "migrations" in root:
                    os.remove(os.path.join(root, file))
                    print(f"Removido: {os.path.join(root, file)}")

def remove_pycache():
    """Remove diretórios e arquivos .pyc e __pycache__."""
    for root, dirs, files in os.walk('.'):
        for dir_name in dirs:
            if dir_name == "__pycache__":
                shutil.rmtree(os.path.join(root, dir_name))
                print(f"Removido: {os.path.join(root, dir_name)}")
        for file in files:
            if file.endswith(".pyc") or file.endswith(".pyo"):
                os.remove(os.path.join(root, file))
                print(f"Removido: {os.path.join(root, file)}")

def collect_static():
    """Coleta arquivos estáticos."""
    call_command('collectstatic', '--noinput')
    print("Arquivos estáticos coletados.")

def migrate_database():
    """Aplica migrações."""
    call_command('makemigrations')
    call_command('migrate', '--run-syncdb')
    print("Migrações aplicadas.")

def main():
    setup_django()
    clear_cache()
    remove_migrations()
    remove_pycache()
    migrate_database()
    collect_static()
    print("Otimização completa.")

if __name__ == "__main__":
    main()
