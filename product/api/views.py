from product.models import ProductCategory, ProductColor, ProductSize, ProductTag
from django.http import JsonResponse
from product.api.serializer import ProductCategorySerializers,ProductSerializer,ProductCreateSerializer,ProductTagSerializer, ProductColorSerializer, ProductSizeSerializer
from product.models import Product
from rest_framework.decorators import api_view
from rest_framework.generics import ListCreateAPIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView


def categories(request):
    categories = ProductCategory.objects.all()
    tags = ProductTag.objects.all()
    tag_serializer = ProductTagSerializer(tags, many=True)
    serializer = ProductCategorySerializers(categories, many=True)

    return JsonResponse(data={"categories": serializer.data, "tags": tag_serializer.data}, safe=False)

@api_view(http_method_names= ['GET', 'POST'])
def products(request):
    products=Product.objects.all()
    if request.method == 'POST':
        serializer = ProductCreateSerializer(data=request.data, context={'request':request})
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(data=serializer.data,status=201)
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
    queryset = Product.objects.all()

    def get_serializer_class(self):
        if self.request.method =='POST':
            return ProductCreateSerializer
        return ProductSerializer

class ProductUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

    def get_serializer_class(self):
        if self.request.method in ['PUT','PATCH']:
            return ProductCreateSerializer
        return ProductSerializer
    
class ProductColorListAPI(ListCreateAPIView):
    serializer_class = ProductColorSerializer
    queryset = ProductColor.objects.all()

    '''def get_serializer_class(self):
        if self.request.method =='POST':
            return ProductColorCreateSerializer
        return ProductSerializer'''
    
class ProductTagListAPI(ListCreateAPIView):
    serializer_class = ProductTagSerializer
    queryset = ProductTag.objects.all()

    '''def get_serializer_class(self):
        if self.request.method =='POST':
            return ProductCreateSerializer
        return ProductSerializer'''
    
class ProductSizeListAPI(ListCreateAPIView):
    serializer_class = ProductSizeSerializer
    queryset = ProductSize.objects.all()

    '''def get_serializer_class(self):
        if self.request.method =='POST':
            return ProductCreateSerializer
        return ProductSerializer'''