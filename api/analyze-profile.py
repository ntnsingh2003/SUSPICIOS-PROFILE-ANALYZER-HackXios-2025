"""
Vercel API endpoint for profile analysis
"""
import sys
import os
import json
from typing import Dict, Any

# Add the backend directory to the Python path
backend_path = os.path.join(os.path.dirname(__file__), '..', 'backend')
sys.path.insert(0, backend_path)

from main import risk_scorer, ProfileData
from fastapi import HTTPException

def handler(request, context):
    """Vercel serverless function handler"""
    
    if request.method != 'POST':
        return {
            'statusCode': 405,
            'body': json.dumps({'error': 'Method not allowed'})
        }
    
    try:
        # Parse request body
        body = json.loads(request.body) if hasattr(request, 'body') else request.json
        
        # Create ProfileData object
        profile = ProfileData(**body)
        
        # Analyze profile
        assessment = risk_scorer.calculate_risk_score(profile)
        
        # Return response
        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': 'POST, OPTIONS',
                'Access-Control-Allow-Headers': 'Content-Type'
            },
            'body': json.dumps({
                'risk_score': assessment.risk_score,
                'risk_level': assessment.risk_level,
                'explanations': assessment.explanations,
                'confidence': assessment.confidence,
                'confidence_explanation': assessment.confidence_explanation,
                'recommended_actions': assessment.recommended_actions
            })
        }
        
    except Exception as e:
        return {
            'statusCode': 500,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps({'error': f'Analysis failed: {str(e)}'})
        }