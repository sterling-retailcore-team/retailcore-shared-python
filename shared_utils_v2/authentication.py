import redis
import json
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.exceptions import AuthenticationFailed
from rest_framework import serializers
from drf_spectacular.contrib.rest_framework_simplejwt import SimpleJWTScheme
from django.conf import settings


class UserData(object):
    is_authenticated = True

    def __init__(self, my_dict):
        my_dict['tenant_id'] = my_dict.get('tenant', None)
        my_dict['firstname'] = my_dict.get('first_name', None)
        my_dict['lastname'] = my_dict.get('last_name', None)
        my_dict['is_active'] = True

        for key in my_dict:
            setattr(self, key, my_dict[key])

def get_auth_user(token):
    redis_client = settings.GET_SESSION_REDIS_CLIENT()

    redis_key = f"SESSION_ID_{token}"
    
    try:
        user_data = redis_client.get(redis_key) 
        if user_data is None:
            raise AuthenticationFailed("User session not found")
        # Decode the JSON data from Redis
        user_info = json.loads(user_data)
        return UserData(user_info)
    except json.JSONDecodeError as err:
        print("Auth Session Invalid user data format", err)
        raise serializers.ValidationError(f"Invalid user data format: {err}") from err

    except redis.RedisError as err:
        print("Auth Session Redis connection error", err)
        raise AuthenticationFailed(f"Redis connection error: {err}") from err
    except AuthenticationFailed:
        raise
    except Exception as err:
        import traceback
        traceback.print_exc()
        raise serializers.ValidationError(f"Error occurred: {err}") from err


class CustomJWTAuthentication(JWTAuthentication):

    def get_validated_token(self, raw_token):
        return raw_token.decode()

    def get_user(self, validated_token):
        return get_auth_user(validated_token)


class CustomJWTAuthenticationScheme(SimpleJWTScheme):
    target_class = CustomJWTAuthentication


# what to use to get value from redis...
# SESSION_ID_{jwt_token} --- this is a key u use to get the info from redis

# the key - SESSION_ID_etugdrthgggu776tjjii8665rfhkiyde46f

# json.decode(key)
