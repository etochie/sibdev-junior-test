import csv

from django.contrib.postgres.aggregates import ArrayAgg
from django.db.models import Sum, F
from django.core.cache import cache
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from apps.core.models import Deal
from apps.core.serializers import DealSerializer


class DealView(APIView):
    def post(self, request):
        csv_file = request.FILES.get('deals')
        try:
            csv_reader = csv.DictReader(
                csv_file.read().decode('utf-8').splitlines()
            )
        except AttributeError:
            return Response(
                {'error': "csv file in 'deals' body key is required"},
                status=status.HTTP_400_BAD_REQUEST
            )
        valid_deals = []

        for row in csv_reader:
            deal = DealSerializer(data=row)
            deal.is_valid(True)
            valid_deals.append(Deal(**row))

        Deal.objects.all().delete()
        Deal.objects.bulk_create(valid_deals)
        cache.delete('deals_data')
        return Response()

    def get(self, request):
        cache_data = cache.get('deals_data')
        if cache_data is not None:
            return Response({'response': cache_data})
        customer_spent_money_all_gems = Deal.objects \
                                            .values(username=F('customer')) \
                                            .annotate(
                                                spent_money=Sum('total'),
                                                gems=ArrayAgg(
                                                    'item',
                                                    distinct=True)) \
                                            .order_by('-spent_money')[:5]
        list_of_gems = []
        for customer in customer_spent_money_all_gems:
            list_of_gems.extend(customer['gems'])

        for customer in customer_spent_money_all_gems:
            for item in customer['gems'][:]:
                if list_of_gems.count(item) < 2:
                    customer['gems'].remove(item)
        cache.set(
            'deals_data',
            customer_spent_money_all_gems
        )

        return Response({'response': customer_spent_money_all_gems})
