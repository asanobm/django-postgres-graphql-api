import graphene
from graphene_django.types import DjangoObjectType
from store.models import Shop, Item, Thumbnail


class ShopType(DjangoObjectType):
    class Meta:
        model = Shop


class ItemType(DjangoObjectType):
    class Meta:
        model = Item


# class ThumbailType(DjangoObjectType):
#     class Meta:
#         model = Thumbnail


class Query(object):
    all_Shops = graphene.List(ShopType)
    all_Items = graphene.List(ItemType)
    # all_thumbnails = graphene.List(ThumbailType)

    def resolve_all_shops(self, info, **kwargs):
        return Shop.objects.all()

    def resolve_all_Items(self, info, **kwargs):
        return Item.objects.select_related('item').all()
