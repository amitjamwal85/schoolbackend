import graphene
import school.schema


class Query(school.schema.Query, graphene.ObjectType):
    pass

class Mutation(school.schema.Mutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)