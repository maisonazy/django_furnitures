from pathlib import Path
import shutil

from django.conf import settings
from django.core.management.base import BaseCommand

from furnitures.models import Product


CATALOG = [
    ('Haven Sectional Sofa', 'Spacious cream sectional with a soft, relaxed finish.', '85000', '1mg2.webp'),
    ('Harbor Corner Set', 'Modern blue-grey corner sofa with a matching ottoman.', '78000', 'img1.webp'),
    ('Cloud Three-Seater', 'Soft, rounded blue sofa made for everyday lounging.', '52000', 'img3.webp'),
    ('Harbor Lounge Set', 'A coordinated sofa and armchair set in cool blue-grey.', '110000', 'img4.webp'),
    ('Royal Blue Sofa', 'Rich blue upholstery with refined gold-tone accents.', '48000', 'img5.jpeg'),
    ('Classic Comfort Sofa', 'Comfortable brown sofa with a timeless, easy-care look.', '45000', 'img6.jpeg'),
    ('Willow Two-Seater', 'Compact beige loveseat with plush cushions for smaller spaces.', '38000', 'img7.webp'),
    ('Sandstone Sofa', 'Warm tan fabric sofa with inviting textured cushions.', '55000', 'img8.jpeg'),
    ('Midnight Modern Sofa', 'Sleek black sofa with clean lines and slim metal legs.', '58000', 'img9.jpeg'),
    ('Heritage Sofa', 'Statement mauve sofa with classic carved wood detailing.', '62000', 'img10.jpeg'),
    ('Blush Curve Sectional', 'Eye-catching curved sectional in soft blush-pink upholstery.', '95000', 'img11.jpeg'),
    ('Urban Grey Corner Set', 'Versatile grey corner seating for a contemporary living room.', '88000', 'img12.jpeg'),
]


class Command(BaseCommand):
    help = 'Import the original furniture catalog into the Product database.'

    def handle(self, *args, **options):
        source_dir = settings.BASE_DIR / 'static' / 'imgs'
        destination_dir = Path(settings.MEDIA_ROOT) / 'products'
        destination_dir.mkdir(parents=True, exist_ok=True)
        created_count = 0

        for name, description, price, filename in CATALOG:
            if Product.objects.filter(name=name).exists():
                continue

            source = source_dir / filename
            if not source.is_file():
                self.stderr.write(self.style.WARNING(f'Skipped {name}: image not found at {source}'))
                continue

            relative_image = Path('products') / filename
            destination = destination_dir / filename
            shutil.copy2(source, destination)
            Product.objects.create(
                name=name,
                description=description,
                price=price,
                image=relative_image.as_posix(),
            )
            created_count += 1

        self.stdout.write(self.style.SUCCESS(f'Imported {created_count} catalog products.'))
