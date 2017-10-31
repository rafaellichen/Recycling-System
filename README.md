# Recycling-System

## Firebase - EasyRecycle
### Using Realtime Database to store information
JSON Tree
```js
{
    "inventory" : {
        "BdgUvz0xgqQS8d0VYLR6vyBCC7j2" : {
            "donate" : {
                "-KxjLBh1jdU6wXH0QLnE" : {
                    "description" : "iPhone X",
                    "type" : "Electronic"
                }
            },
            "recycle" : {
                "-KxjLL8SZ9eunklEAQc_" : {
                    "description" : "newspaper",
                    "type" : "Paper"
                }
            }
        }
    },
    "search" : {
        "BdgUvz0xgqQS8d0VYLR6vyBCC7j2" : {
            "check" : ""
        }
    },
    "users" : {
        "BdgUvz0xgqQS8d0VYLR6vyBCC7j2" : {
            "city" : "Universe",
            "first_name" : "RAFAEL",
            "last_name" : "LI CHEN",
            "phone" : "1234567890",
            "state" : "New York",
            "street1" : "1234 Earth Av",
            "street2" : "",
            "zip" : "12345"
        }
    }
}
```
### Deployed using Firebase Hosting service
[Easy Recycle](https://recycling-system.firebaseapp.com/ )
***
## recycleApp
**cd into the recycling-system**:
> $ python manage.py runserver
