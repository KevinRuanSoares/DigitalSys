# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import permissions


class Admin(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.profile == 'ADMIN'

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.profile == 'ADMIN'