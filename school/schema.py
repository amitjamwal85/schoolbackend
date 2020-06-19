import graphene
from graphene_django.types import DjangoObjectType, ObjectType
from school.models import School

'''********************************** GraphQL Types **********************************'''

class SchoolType(DjangoObjectType):
    class Meta:
        model = School


'''********************************** Mutation **********************************'''

class SchoolInput(graphene.InputObjectType):
    id = graphene.UUID()
    school_name = graphene.String()
    school_address = graphene.String()
    school_phone = graphene.String()


class CreateSchool(graphene.Mutation):
    class Arguments:
        input = SchoolInput(required=True)

    ok = graphene.Boolean()
    school = graphene.Field(SchoolType)

    @staticmethod
    def mutate(root, info, input=None):
        ok = True
        school_instance = School(school_name=input.school_name,
                                 school_address=input.school_address,
                                 school_phone=input.school_phone
                                 )
        school_instance.save()
        return CreateSchool(ok=ok, school=school_instance)



class UpdateSchool(graphene.Mutation):
    class Arguments:
        id = graphene.UUID(required=True)
        input = SchoolInput(required=True)

    ok = graphene.Boolean()
    school = graphene.Field( SchoolType )

    @staticmethod
    def mutate(root, info, id, input=None):
        ok = False
        school_instance = School.objects.get(pk=id)
        if school_instance:
            ok = True
            school_instance.school_name = input.school_name
            school_instance.school_address = input.school_address
            school_instance.school_phone = input.school_phone
            school_instance.save()
            return UpdateSchool(ok=ok, school=school_instance)
        return UpdateSchool(ok=ok, actor=None)



class DeleteSchool(graphene.Mutation):
    class Arguments:
        id = graphene.UUID(required=True)

    ok = graphene.Boolean()

    @staticmethod
    def mutate(root, info, id):
        ok = False
        try:
            school_instance = School.objects.get(pk=id)
        except School.DoesNotExist:
            school_instance = None

        if school_instance:
            ok = True
            school_instance.delete()
            return DeleteSchool(ok=ok)
        return DeleteSchool(ok=ok)

class Mutation(graphene.ObjectType):
    create_school = CreateSchool.Field()
    update_school = UpdateSchool.Field()
    delete_school = DeleteSchool.Field()

'''************************************* Query ***************************************'''

class Query(ObjectType):
    school = graphene.Field( SchoolType, id=graphene.UUID() )
    schools = graphene.List( SchoolType )

    def resolve_school(self, info, **kwargs):
        id = kwargs.get( "id" )
        if id is not None:
            return School.objects.get(pk=id)
        return None

    def resolve_schools(self, info, **kwargs):
        return School.objects.all()
