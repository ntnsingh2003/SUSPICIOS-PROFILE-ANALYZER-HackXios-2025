"""
Vercel API endpoint for demo data
"""
import json

def handler(request, context):
    """Vercel serverless function handler for demo data"""
    
    if request.method != 'GET':
        return {
            'statusCode': 405,
            'body': json.dumps({'error': 'Method not allowed'})
        }
    
    demo_data = {
        "legitimate_profile": {
            "account_age_days": 365,
            "followers": 250,
            "following": 180,
            "post_count": 120,
            "profile_completed": True,
            "messages": [
                "Thanks for connecting! Looking forward to networking.",
                "Great article you shared about industry trends."
            ]
        },
        "suspicious_profile": {
            "account_age_days": 45,
            "followers": 15,
            "following": 800,
            "post_count": 200,
            "profile_completed": False,
            "messages": [
                "Hello! I'm new to this platform.",
                "Looking to connect with professionals in your field.",
                "Would love to discuss potential opportunities."
            ]
        },
        "romance_scam_profile": {
            "account_age_days": 7,
            "followers": 2,
            "following": 500,
            "post_count": 50,
            "profile_completed": False,
            "messages": [
                "My darling, I love you so much already.",
                "I am engineer working on oil rig, need emergency money.",
                "Trust me honey, send Western Union transfer immediately."
            ]
        }
    }
    
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'GET, OPTIONS',
            'Access-Control-Allow-Headers': 'Content-Type'
        },
        'body': json.dumps(demo_data)
    }