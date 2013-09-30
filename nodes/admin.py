from django.contrib import admin

from nodes.models import Node,Title

class NodeAdmin(admin.ModelAdmin):
    list_display = ["title","user","inherit","content","status"]


admin.site.register(Node, NodeAdmin)
admin.site.register(Title)
