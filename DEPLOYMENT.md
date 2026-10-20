# Deploying on Vercel

Vercel detects this Django project from `manage.py` and serves Django static
assets through its CDN. The project root to select when importing the GitHub
repository is the repository root (the directory containing `manage.py`).

## 1. Create a Vercel project

Import `maisonazy/django_furnitures` from the Vercel dashboard. Keep the
framework preset on **Django** or **Other** if Django is not detected. No
custom build command or `vercel.json` is needed for Vercel's current Django
support.

## 2. Add production environment variables

Add these under **Project Settings → Environment Variables** for Production
and Preview:

| Name | Value |
| --- | --- |
| `DEBUG` | `False` |
| `DJANGO_SECRET_KEY` | A newly generated, private Django secret key |
| `DATABASE_URL` | A PostgreSQL connection URL from a Vercel Marketplace provider such as Neon or Supabase |

You can generate a secret locally with:

```sh
python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
```

The settings also recognize `POSTGRES_URL` if that is the variable supplied by
your database integration. Keep the database connection string private.

For a custom domain, add the domain to `ALLOWED_HOSTS` as well as
`CSRF_TRUSTED_ORIGINS`, for example:

```text
ALLOWED_HOSTS=shop.example.com
CSRF_TRUSTED_ORIGINS=https://shop.example.com
```

## 3. Initialize the database

After adding the environment variables, deploy once and run migrations against
the production database from a trusted local checkout with the Vercel
environment loaded:

```sh
vercel env pull .env.local
set -a
. ./.env.local
set +a
python manage.py migrate
```

To copy the products currently in the local SQLite database, export a fixture
locally before connecting to production, then load it after running migrations:

```sh
python manage.py dumpdata furnitures.Product --indent 2 > products.json
```

With the production environment loaded, run:

```sh
python manage.py loaddata products.json
```

Product image files already committed under `media/products/` are included as
static assets. Vercel's filesystem is not persistent, so images uploaded later
through Django admin need external object storage before using admin uploads in
production.

## 4. Deploy

Push the deployment changes to GitHub, then use Vercel's first deployment or
trigger a redeploy. Vercel will create preview deployments for other branches
and production deployments for the configured production branch.

The existing SQLite database stays useful for local development. Production
requires PostgreSQL so catalog, session, and admin data survive deployments.
