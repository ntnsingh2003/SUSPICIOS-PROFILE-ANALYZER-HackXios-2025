# Deployment Guide: Suspicious Profile Analyzer

## 🚀 Vercel Deployment

This project is configured for deployment on Vercel with both frontend (React) and backend (FastAPI) components.

### Prerequisites

1. **Vercel Account**: Sign up at [vercel.com](https://vercel.com)
2. **GitHub Repository**: Push your code to GitHub
3. **Vercel CLI** (optional): `npm install -g vercel`

### Deployment Steps

#### Option 1: Deploy via Vercel Dashboard (Recommended)

1. **Connect Repository**:
   - Go to [vercel.com/dashboard](https://vercel.com/dashboard)
   - Click "New Project"
   - Import your GitHub repository

2. **Configure Project**:
   - Framework Preset: "Other"
   - Root Directory: `./` (leave empty)
   - Build Command: `npm run build`
   - Output Directory: `frontend/build`

3. **Environment Variables** (if needed):
   - No environment variables required for basic deployment

4. **Deploy**:
   - Click "Deploy"
   - Vercel will automatically build and deploy your project

#### Option 2: Deploy via CLI

```bash
# Install Vercel CLI
npm install -g vercel

# Login to Vercel
vercel login

# Deploy from project root
vercel

# Follow the prompts:
# - Set up and deploy? Y
# - Which scope? (select your account)
# - Link to existing project? N
# - Project name: suspicious-profile-analyzer
# - Directory: ./
# - Override settings? N
```

### Project Structure for Vercel

```
suspicious-profile-analyzer/
├── api/                     # Serverless API functions
│   ├── analyze-profile.py   # Profile analysis endpoint
│   └── demo-data.py         # Demo data endpoint
├── frontend/                # React application
│   ├── src/
│   ├── public/
│   └── package.json
├── backend/                 # FastAPI source code
│   ├── main.py
│   └── requirements.txt
├── vercel.json             # Vercel configuration
├── package.json            # Root package.json for build
└── requirements.txt        # Python dependencies
```

### Vercel Configuration

The `vercel.json` file configures:
- **Python API Functions**: Serverless functions for backend logic
- **Static Build**: React frontend build process
- **Routing**: API routes (`/api/*`) and static file serving
- **CORS**: Cross-origin resource sharing for API access

### API Endpoints

Once deployed, your API will be available at:
- `https://your-project.vercel.app/api/analyze-profile` - Profile analysis
- `https://your-project.vercel.app/api/demo-data` - Demo data

### Frontend

The React application will be served at:
- `https://your-project.vercel.app/` - Main application

### Troubleshooting

#### Common Issues

1. **Build Failures**:
   - Check that all dependencies are listed in `requirements.txt`
   - Ensure Python version compatibility (3.9+)
   - Verify frontend builds locally: `cd frontend && npm run build`

2. **API Errors**:
   - Check Vercel function logs in dashboard
   - Verify CORS configuration for your domain
   - Test API endpoints individually

3. **Import Errors**:
   - Ensure all Python modules are properly imported
   - Check that backend code is accessible from API functions

#### Vercel Limits

- **Function Timeout**: 10 seconds (Hobby plan)
- **Function Size**: 50MB unzipped
- **Bandwidth**: 100GB/month (Hobby plan)

### Custom Domain (Optional)

1. **Add Domain**:
   - Go to Project Settings → Domains
   - Add your custom domain
   - Configure DNS records as instructed

2. **SSL Certificate**:
   - Automatically provisioned by Vercel
   - No additional configuration needed

### Monitoring

- **Analytics**: Available in Vercel dashboard
- **Function Logs**: Real-time logs for debugging
- **Performance**: Core Web Vitals tracking

## 🔧 Local Development

### Backend
```bash
cd backend
pip install -r requirements.txt
python main.py
# Server runs on http://localhost:8000
```

### Frontend
```bash
cd frontend
npm install
npm start
# App runs on http://localhost:3000
```

## 📊 Production Considerations

### Performance
- API functions are serverless (cold start ~1-2 seconds)
- Frontend is served via Vercel's global CDN
- ML model loads on first request (cached afterward)

### Security
- CORS configured for production domains
- No sensitive data stored in client-side code
- API rate limiting handled by Vercel

### Scaling
- Automatic scaling based on traffic
- No server management required
- Pay-per-use pricing model

---

**Ready for hackathon judges and live demonstrations!**