from django.db import models

class AssetChildManager(models.Manager):
    def children(self, parent_id):
        return self.get_queryset().raw(
            """
            with resursive parent_assets(id) as (
                select assets.id 
                from assets
                where id = %s
            union
                select assets.id
                from assets, parent_assets
                where assets.parent_id = parent_assets.id
            )
            select id from parent_assets
            """, 
            [parent_id])
    
    
class AssetQuerySet(models.QuerySet):
    pass

AssetManager = AssetChildManager.from_queryset(AssetQuerySet)