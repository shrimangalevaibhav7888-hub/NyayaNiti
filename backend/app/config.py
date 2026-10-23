from pydantic_settings import BaseSettings
from typing import List

class Settings(BaseSettings):
    APP_NAME: str = "NyayaNiti — AICTE Institution Complaint Monitoring & Coordination System"
    API_V1_PREFIX: str = "/api"
    SECRET_KEY: str = "nyayaniti-secret-key-prod-demo-change-in-env-981247"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 1440  # 24 hours
    
    DATABASE_URL: str = "sqlite:///./nyayaniti.db"
    
    CORS_ORIGINS: List[str] = [
        "http://localhost:5173",
        "http://127.0.0.1:5173",
        "http://localhost:3000",
        "http://127.0.0.1:3000"
    ]
    
    # Matching and AI parameters
    SBERT_MODEL_NAME: str = "all-MiniLM-L6-v2"
    OVERLAP_HIGH_THRESHOLD: float = 0.82
    OVERLAP_REVIEW_THRESHOLD: float = 0.60
    RAPIDFUZZ_NAME_SIMILARITY_THRESHOLD: float = 78.0
    
    # Complaint Surge Thresholds
    SURGE_Z_SCORE_THRESHOLD: float = 1.8
    SURGE_MIN_COMPLAINT_COUNT: int = 3
    SURGE_WINDOW_DAYS: int = 30
    
    # SLA Prescribed Deadlines (days)
    SLA_CRITICAL_DAYS: int = 7
    SLA_HIGH_DAYS: int = 15
    SLA_MEDIUM_DAYS: int = 30
    SLA_LOW_DAYS: int = 45
    
    class Config:
        env_file = ".env"
        extra = "allow"

settings = Settings()
