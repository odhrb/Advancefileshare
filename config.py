import os
from typing import List, Optional

class Config:
    # Bot Configuration
    BOT_TOKEN: str = os.environ.get("BOT_TOKEN", "")
    BOT_USERNAME: str = os.environ.get("BOT_USERNAME", "")
    
    # Database Configuration
    MONGODB_URL: str = os.environ.get("MONGODB_URL", "mongodb://localhost:27017")
    DB_NAME: str = os.environ.get("DB_NAME", "telegram_file_bot")
    
    # Web Server Configuration
    WEB_SERVER_ENABLED: bool = os.environ.get("WEB_SERVER_ENABLED", "true").lower() == "true"
    WEB_PORT: int = int(os.environ.get("PORT", 5000))
    SESSION_SECRET: str = os.environ.get("SESSION_SECRET", "your-secret-key-here")
    
    # Admin Configuration
    ADMIN_IDS: List[int] = [int(x) for x in os.environ.get("ADMIN_IDS", "").split(",") if x.strip()]
    
    # Force Subscription Configuration
    FORCE_SUB_CHANNELS: List[str] = [x.strip() for x in os.environ.get("FORCE_SUB_CHANNELS", "").split(",") if x.strip()]
    
    # File Configuration
    MAX_FILE_SIZE: int = int(os.environ.get("MAX_FILE_SIZE", "2147483648"))  # 2GB
    AUTO_DELETE_TIME: int = int(os.environ.get("AUTO_DELETE_TIME", "0"))  # 0 means no auto-delete
    
    # Storage Configuration
    STORAGE_CHANNEL: str = os.environ.get("STORAGE_CHANNEL", "")
    
    # Security Configuration
    ENCRYPTION_KEY: str = os.environ.get("ENCRYPTION_KEY", "")
    
    # Rate Limiting
    RATE_LIMIT_ENABLED: bool = os.environ.get("RATE_LIMIT_ENABLED", "true").lower() == "true"
    RATE_LIMIT_REQUESTS: int = int(os.environ.get("RATE_LIMIT_REQUESTS", "10"))
    RATE_LIMIT_WINDOW: int = int(os.environ.get("RATE_LIMIT_WINDOW", "60"))
    
    # Premium Features
    PREMIUM_ENABLED: bool = os.environ.get("PREMIUM_ENABLED", "false").lower() == "true"
    PREMIUM_SUBSCRIPTION_PRICE: float = float(os.environ.get("PREMIUM_SUBSCRIPTION_PRICE", "5.0"))
    
    # Localization
    DEFAULT_LANGUAGE: str = os.environ.get("DEFAULT_LANGUAGE", "en")
    
    # Logging
    LOG_LEVEL: str = os.environ.get("LOG_LEVEL", "INFO")
    LOG_FILE: str = os.environ.get("LOG_FILE", "bot.log")
    
    # Redis Configuration (for caching)
    REDIS_URL: str = os.environ.get("REDIS_URL", "redis://localhost:6379")
    REDIS_ENABLED: bool = os.environ.get("REDIS_ENABLED", "false").lower() == "true"
    
    # Deployment Configuration
    WEBHOOK_URL: str = os.environ.get("WEBHOOK_URL", "")
    WEBHOOK_PATH: str = os.environ.get("WEBHOOK_PATH", "/webhook")
    
    # Branding
    BOT_NAME: str = os.environ.get("BOT_NAME", "File Sharing Bot")
    BOT_DESCRIPTION: str = os.environ.get("BOT_DESCRIPTION", "Premium Telegram File Sharing Bot")
    
    @classmethod
    def validate_config(cls) -> bool:
        """Validate essential configuration"""
        if not cls.BOT_TOKEN:
            raise ValueError("BOT_TOKEN is required")
        if not cls.MONGODB_URL:
            raise ValueError("MONGODB_URL is required")
        return True
        
    @classmethod
    def get_force_sub_channels(cls) -> List[str]:
        """Get list of force subscription channels"""
        return cls.FORCE_SUB_CHANNELS[:10]  # Maximum 10 channels
        
    @classmethod
    def is_admin(cls, user_id: int) -> bool:
        """Check if user is admin"""
        return user_id in cls.ADMIN_IDS
        
    @classmethod
    def get_web_config(cls) -> dict:
        """Get web configuration"""
        return {
            'SECRET_KEY': cls.SESSION_SECRET,
            'MONGODB_URL': cls.MONGODB_URL,
            'DB_NAME': cls.DB_NAME,
            'WEB_PORT': cls.WEB_PORT,
            'BOT_NAME': cls.BOT_NAME,
            'BOT_DESCRIPTION': cls.BOT_DESCRIPTION
        }
