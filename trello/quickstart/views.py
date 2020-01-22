from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.shortcuts import render
from rest_framework import viewsets
import requests
from rest_framework.decorators import api_view


class BoardView(APIView):
     def get(self, request):
        url = "https://api.trello.com/1/members/me/boards"
        querystring = {"fields":"name","key":"15c9e2b50335dd89210080ef7546f484","token":"2e4e3156fd4139795c88a038d6094105afa7173cf42d4f95cac61cd30edcf8b0"}
        response = requests.request("GET", url, params=querystring)
        return Response(response)

class OrganizationView(APIView):
     def get(self, request):
        url = "https://api.trello.com/1/members/me/organizations"
        querystring = {"fields":"name","key":"15c9e2b50335dd89210080ef7546f484","token":"2e4e3156fd4139795c88a038d6094105afa7173cf42d4f95cac61cd30edcf8b0"}
        response = requests.request("GET", url, params=querystring)
        return Response(response)

class ListView(APIView):
     def get(self, request):
        url = "https://api.trello.com/1/boards/5e20e57e8132ad103f100425/lists"
        querystring = {"cards":"none","card_fields":"all","filter":"open","fields":"all","key":"15c9e2b50335dd89210080ef7546f484","token":"2e4e3156fd4139795c88a038d6094105afa7173cf42d4f95cac61cd30edcf8b0"}
        response = requests.request("GET", url, params=querystring)
        return Response(response)        

class CreateCardView(APIView):
     def get(self, request):
        url = "https://api.trello.com/1/cards"
        querystring = {"name":"Card title","desc":"Card description","idList":"5e20e57e8132ad103f100426","keepFromSource":"all","key":"15c9e2b50335dd89210080ef7546f484","token":"2e4e3156fd4139795c88a038d6094105afa7173cf42d4f95cac61cd30edcf8b0"}
        response = requests.request("POST", url, params=querystring)

        return Response(response)        