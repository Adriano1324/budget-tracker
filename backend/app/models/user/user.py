from neomodel import StringProperty, StructuredNode, UniqueIdProperty


class User(StructuredNode):
    uid = UniqueIdProperty()
    name = StringProperty(unique_index=True)
    avatar_src = StringProperty()
    password = StringProperty()
