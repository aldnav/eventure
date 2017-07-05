

class ActivitySerializer(object):

    def serialize(self, instance, fields):
        serialized = {}
        for field in fields:
            try:
                serialized[field] = getattr(instance, field, None)
            except Exception as e:
                print e
        return serialized

activity_serializer = ActivitySerializer()
