import json

from core.renderers import ConduitJSONRenderer


class UserJSONRenderer(ConduitJSONRenderer):
    # charset = 'utf-8'
    object_label = 'user'

    def render(self, data, accepted_media_type=None, renderer_context=None):
        token = data.get('token', None)

        if token is not None and isinstance(token, bytes):
            data['token'] = token.decode('utf-8')

        # return json.dumps({
        #     'user': data
        # })

        return super(UserJSONRenderer, self).render(data)
