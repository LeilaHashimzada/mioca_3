from product.models import ProductCategory
from django.http import JsonResponse
from product.api.serializer import ProductCategorySerializers,ProductSerializer,ProductCreateSerializer,ProductTagSerializer
from product.models import Product
from rest_framework.decorators import api_view
from rest_framework.generics import ListCreateAPIView
from rest_framework.generics import RetrieveUpdateAPIView


def categories(request):
    categories = ProductCategory.objects.all()
    tags = ProductTagSerializer(many=True)
    serializer = ProductCategorySerializers(categories, many=True)
#     category_dict = []
#     for category in categories:
#         if category.parent:
#             category_dict.append(
#                 {'parent':category.parent.id,
#                 'id':category.id,
#                 'title': category.title,
#                 }
#             )
#         else:
#                 category_dict.append(
#                 {'id':category.id,
#                 'title': category.title,
#                 }
#             )

    return JsonResponse(data= serializer.data, safe=False)

@api_view(http_method_names= ['GET', 'POST'])
def products(request):
    products=Product.objects.all()
    if request.method == 'POST':
        serializer = ProductCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(data=serializer.data,status=200)
            
        return JsonResponse(data=serializer.errors,status=400)


    serializer = ProductSerializer(products,context = {'request':request},many=True)
    return JsonResponse(data= serializer.data, safe=False)

@api_view(http_method_names = ['PUT','PATCH'])
def product_update(request,pk):
    product=Product.objects.get(id = pk)
    if request.method == 'PUT':
        serializer = ProductCreateSerializer(data = request.data, context = {'request':request},instance=product)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(data=serializer.data,status=201)
        return JsonResponse(data=serializer.errors,status=400)
    if request.method =='PATCH':
        serializer = ProductCreateSerializer(data = request.data,instance=product,partial=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(data=serializer.data,status=201)
        return JsonResponse(data=serializer.errors,status=400)
    serializer = ProductSerializer(products,context = {'request':request},many=True)
    return JsonResponse(data = serializer.data,safe=False)

class ProductListAPI(ListCreateAPIView):
    serializer_class = ProductSerializer
    queryset = ProductSerializer

    def get_serializer_class(self):
        if self.request.method =='POST':
            return ProductCreateSerializer
        return ProductSerializer

class ProductUpdateAPIView(RetrieveUpdateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

    def get_serializer_class(self):
        if self.request.method in ['PUT','PATCH']:
            return ProductCreateSerializer
        return ProductSerializer
    