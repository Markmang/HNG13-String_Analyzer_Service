from rest_framework import serializers
from .models import AnalyzedString
from .utils import analyze_string

class AnalyzedStringSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnalyzedString
        fields = '__all__'
        read_only_fields = [
            'sha256_hash',
            'length',
            'is_palindrome',
            'unique_characters',
            'word_count',
            'character_frequency_map',
            'created_at',
        ]

    def validate_value(self, value):
        if not isinstance(value, str):
            raise serializers.ValidationError("Value must be a string.")
        if not value.strip():
            raise serializers.ValidationError("Value cannot be empty or whitespace.")
        return value

    def create(self, validated_data):
        value = validated_data.get("value")
        analysis = analyze_string(value)

        # Check if it already exists
        if AnalyzedString.objects.filter(sha256_hash=analysis["sha256_hash"]).exists():
            raise serializers.ValidationError({"detail": "String already exists in the system."})

        # Create the analyzed string record
        return AnalyzedString.objects.create(
            value=value,
            sha256_hash=analysis["sha256_hash"],
            length=analysis["length"],
            is_palindrome=analysis["is_palindrome"],
            unique_characters=analysis["unique_characters"],
            word_count=analysis["word_count"],
            character_frequency_map=analysis["character_frequency_map"],
        )
