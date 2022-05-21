import re
from rest_framework import serializers
from .models import ApartmentType,Apartment,Building



class ApartmentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApartmentType
        fields = [
            "id",
            "type",
          
        ]


class BuildingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Building
        fields = [
            "id",
            "title",
          
        ]

class ApartmentSerializer(serializers.ModelSerializer):
    apartment_type=ApartmentTypeSerializer()

    building=BuildingSerializer()



    class Meta:
        model = Apartment
        fields = [
            "id",
            "name",
            "description",
            "apartment_type",
            "building"
        ]
        # depth = 1

    def create(self, validated_data):

        apartment_type_data=validated_data.pop("apartment_type")

        building_data=validated_data.pop("building")

        apartmentType_model=ApartmentType.objects.create(**apartment_type_data)

        building_model=Building.objects.create(**building_data)

        apartment=Apartment.objects.create(apartment_type=apartmentType_model,
                                            building=building_model,
                                            **validated_data)
        return apartment


    def update(self, instance, validated_data):

        apartment_type_data=validated_data.pop("apartment_type")

        building_data=validated_data.pop("building")


        apartment_type=instance.apartment_type
        building=instance.building

        for k,v in apartment_type_data.items():
            setattr(apartment_type,k,v)
        apartment_type.save()

        for k,v in building_data.items():
            setattr(building,k,v)
        building.save()


        
        instance.name=validated_data.get("name",instance.name)
        instance.description=validated_data.get("description",instance.description)
        instance.apartment_type=validated_data.get("type",instance.apartment_type)
        instance.building=validated_data.get("title",instance.building)

        instance.save()
        return instance

    

 






        

    