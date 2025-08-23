# books/versioning.py
from rest_framework.versioning import BaseVersioning

class CombinedVersioning(BaseVersioning):
    """
    Determine version from (in priority):
      1. URL path capture `version` (e.g. /api/<version>/...)
      2. Query param `version` or `v` (e.g. ?version=v2 or ?v=2)
      3. Header 'X-API-Version'
      default: 'v1'
    """
    def determine_version(self, request, *args, **kwargs):
        # 1) URL path (kwargs)
        if kwargs and 'version' in kwargs:
            return kwargs.get('version')

        # 2) query param
        q = request.query_params.get('version') or request.query_params.get('v')
        if q:
            return str(q)

        # 3) header
        hv = request.headers.get('X-API-Version') or request.headers.get('X_API_VERSION')
        if hv:
            return str(hv)

        return 'v1'
