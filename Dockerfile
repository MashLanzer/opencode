FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    git \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first for better caching
COPY requirements.txt /app/ 2>/dev/null || true

# Install Python dependencies
RUN pip install --no-cache-dir python-telegram-bot requests python-dotenv aiohttp

# Copy application files
COPY telegram-bot.py /app/
COPY cal-integration.py /app/

# Set environment variables
ENV TELEGRAM_TOKEN=7953249856:AAGLm38BnrqtFjgSCO952wAglmtEjyzAWcs
ENV CHAT_ID=5667291055
ENV CAL_API_KEY=cal_live_9643088a06b3a5a774337b5e40485f93
ENV OBSIDIAN_URL=http://host.docker.internal:27123
ENV OBSIDIAN_API_KEY=dadde3d8184f6aae78239eb4570ac4430b55532fcf5afb77fd081f70c7e0c459
ENV OMI_API_KEY=omi_dev_f109295456f5a35b2226ddadc206b4dc

# Expose port for health check
EXPOSE 8080

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:8080/health || exit 1

# Run the bot
CMD ["python", "telegram-bot.py"]