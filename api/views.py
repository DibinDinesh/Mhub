from django.shortcuts import render

from rest_framework.views import APIView

from rest_framework.response import Response

from rest_framework import viewsets

from api.serializers import MovieSerializer,ActorSerializer,AlbumSerializer,AddTrackSerializer,ReviewSerializer

from rest_framework.decorators import action

from myapp.models import Movie,Actor,Album,Tracks,Review



class MovieListCreateView(APIView):

    def get(self,request,*args,**kwargs):

        qs=Movie.objects.all()

        serializer_instance=MovieSerializer(qs,many=True)
                            #serialization-method
        return Response(data=serializer_instance.data)
    
    def post(self,request,*args,**kwargs):

        serializer_instance=MovieSerializer(data=request.data)
                        #deserialization-method

        if serializer_instance.is_valid():

            serializer_instance.save()

            return Response(data=serializer_instance.data)
        else:

            return Response(data=serializer_instance.errors)


class MovieRetriveUpdateDestroyView(APIView):

    def get(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        movie_obj=Movie.objects.get(id=id)

        serializer_instance=MovieSerializer(movie_obj,many=False)

        return Response(data=serializer_instance.data)
    

    def put(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        movie_obj=Movie.objects.get(id=id)

        serializer_instance=MovieSerializer(data=request.data,instance=movie_obj)

        if serializer_instance.is_valid():

            serializer_instance.save()

            return Response(data=serializer_instance.data)
        
        else:

            return Response(data=serializer_instance.errors)


    def delete(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        obj=Movie.objects.get(id=id)

        obj.delete()

        return Response(data={"message":"movie deleted"})
    

class LanguagesView(APIView):

    def get(self,request,*args,**kwargs):

        qs=Movie.objects.all().values_list("language",flat=True).distinct()
                                                                #-no need duplicate list
        return Response(data=qs)
    
class GenreListView(APIView):

    def get(self,request,*args,**kwargs):

        qs=Movie.objects.all().values_list("genre",flat=True).distinct()

        return Response(data=qs)
    
class ActorViewSet(viewsets.ViewSet):
    # Using --viewset

    def list(self,request,*args,**kwargs):

        qs=Actor.objects.all()

        serializer_instance=ActorSerializer(qs,many=True)

        return Response(data=serializer_instance.data)
    
    def create(self,request,*args,**kwargs):

        serializer_instance=ActorSerializer(data=request.data)

        if serializer_instance.is_valid():

            serializer_instance.save()

            return Response(data=serializer_instance.data)
        else:

            return Response(data=serializer_instance.errors)
        
    def retrieve(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        actor_obj=Actor.objects.get(id=id)

        serializer_instance=ActorSerializer(actor_obj,many=False)

        return Response(data=serializer_instance.data)
    
    def update(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        actor_obj=Actor.objects.get(id=id)

        serializer_instance=ActorSerializer(data=request.data,instance=actor_obj)

        if serializer_instance.is_valid():

            serializer_instance.save()

            return Response(data=serializer_instance.data)
        else:

            return Response(data=serializer_instance.errors)

    def destroy(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        actor_obj=Actor.objects.get(id=id)

        actor_obj.delete()

        return Response(data={"message":"deleted"})


# Using modelviewset
#list,detail view,update,delete all are defined modelviewset
#custom method also defined
#eg :   def language(self,request,*args,**kwargs):
class MovieViewSet(viewsets.ModelViewSet):

    serializer_class=MovieSerializer

    queryset=Movie.objects.all()

    
class AlbumViewSet(viewsets.ModelViewSet):

    serializer_class=AlbumSerializer

    queryset=Album.objects.all()

    @action(methods=["GET"],detail=False)
    def languages(self,request,*args,**kwargs):

        qs=Album.objects.all().values_list("language",flat=True).distinct() #no duplicate list

        return Response(data=qs)

    @action(methods=["GET"],detail=False)#no url id,so false, if have id use true
    def directors(self,request,*args,**kwargs):

        qs=Album.objects.all().values_list("director",flat=True).distinct()

        return Response(data=qs)
    
    @action(methods=["POST"],detail=True)#have url id,so true
    def add_track(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        album_obj=Album.objects.get(id=id)

        serializer_instance=AddTrackSerializer(data=request.data)
                            #deserialization
        if serializer_instance.is_valid():

            serializer_instance.save(album_object=album_obj)

            return Response(data=serializer_instance.data)
        
        else:

            return Response(data=serializer_instance.errors)

    @action(methods=["POST"],detail=True)
    def add_review(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        album_obj=Album.objects.get(id=id)

        serializer_instance=ReviewSerializer(data=request.data)#-deserialization

        if serializer_instance.is_valid():

            serializer_instance.save(album_object=album_obj)

            return Response(data=serializer_instance.data)
        else:

            return Response(data=serializer_instance.errors)


class TrackViewSetView(viewsets.ModelViewSet):

    serializer_class=AddTrackSerializer

    queryset=Tracks.objects.all()




