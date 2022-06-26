import uuid
import datetime
from .models import Main
from rest_framework.views import APIView
from rest_framework.response import Response

class ApiView(APIView):
    def post(self, request):
        updateDate = request.data['updateDate']
        for item in request.data['items']:
            parentId = None
            price = None
            id = item['id']
            name = item['name']
            type = item['type']
            if type not in ("CATEGORY", "OFFER"):
                return Response({"code": 400, "message": "Validation Failed"}, status=400)

            if 'parentId' in item and item['parentId'] != None:
                parentId = item['parentId']
                try:
                    if not Main.objects.filter(uid=parentId).exists():
                        return Response({"code": 400, "message": "Validation Failed"}, status=400)
                    else:
                        parentId = Main.objects.filter(uid=parentId)[0]
                        parent = parentId
                        while parent!=None:
                            parent.updateDate = updateDate
                            parent.save()
                            parent = parent.parentId
                except:
                    return Response({"code": 400, "message": "Validation Failed"}, status=400)

            if 'price' in item:
                price = item['price']
            if Main.objects.filter(uid=id).exists():
                try:
                    obj = Main.objects.filter(uid=id)[0]
                    obj.name = name
                    obj.type = type
                    if 'parentId' in item:
                        obj.parentId = parentId
                    if 'price' in item:
                        obj.price = price
                    obj.updateDate = updateDate
                    obj.save()
                except:
                    return Response({"code": 400, "message": "Validation Failed"}, status=400)
            else:
                try:
                    Main.objects.create(uid=id, name=name, type=type, parentId=parentId, price=price, updateDate=updateDate)
                except:
                    return Response({"code": 400, "message": "Validation Failed"}, status=400)

        return Response({"code": 200, "message": "Sucessfull"}, status=200)

    def delete(self, request, uid):
        try:
            if Main.objects.filter(uid = uid).exists():
                obj = Main.objects.filter(uid=uid)[0]
                obj.delete()
            else:
                return Response({"code": 404, "message": "Item not found"}, status=404)
        except:
            return Response({"code": 400, "message": "Validation Failed"}, status=400)
        return Response({"code": 200, "message": "Successful"}, status=200)

    def get(self, request, uid):
        try:
            if Main.objects.filter(uid = uid).exists():
                obj = Main.objects.filter(uid=uid)[0]
                ans = {}
                def dfs(v, dic):
                    if type(dic) == type([]):
                        dic.append({})
                        dic = dic[-1]
                    dic['id'] = v.uid
                    dic['name'] = v.name
                    dic['type'] = v.type
                    if v.parentId == None:
                        dic['parentId'] = None
                    else:
                        dic['parentId'] = v.parentId.uid

                    if v.price != None:
                        dic['price'] = v.price
                    dic['date'] = v.updateDate
                    dic['children'] = []
                    summ, col = 0, 0
                    for item in Main.objects.filter(parentId = v):
                        lst = dfs(item, dic['children'])
                        summ += lst[1]
                        col += lst[0]
                    if len(dic['children']) == 0:
                        dic['children'] = None
                    if v.price != None:
                        return [1, v.price]
                    else:
                        dic['price'] = summ//col
                        return [col, summ]
                dfs(obj, ans)
                return Response(ans)
            else:
                return Response({"status_code": 404, "detail": "Item not found"}, status=404)
        except:
            return Response({"status_code": 400, "detail": "Validation Failed"}, status=400)

class OptionalApiView(APIView):
    def get(self,request):
        print(request)
        try:
            this_date = request.GET.get('date')
            if '.' in this_date:
                r = datetime.datetime.strptime(this_date, "%Y-%m-%dT%H:%M:%S.%f%z")
            else:
                r = datetime.datetime.strptime(this_date, "%Y-%m-%dT%H:%M:%S%z")
            date_created = r-datetime.timedelta(days=1)
            query = Main.objects.filter(updateDate__gt = date_created, type='OFFER')
            ans = {"items": []}
            for item in query:
                parentID = None
                if item.parentId != None:
                    parentID = item.parentId.uid
                ans['items'].append({'id':item.uid, 'name':item.name, 'date':item.updateDate, 'parentId':parentID, 'price':item.price, 'type':item.type})
            return Response(ans)
        except:
            return Response({"status_code": 400, "detail": "Validation Failed"}, status=400)