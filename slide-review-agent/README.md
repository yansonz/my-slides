# 슬라이드 검토 도우미 Agent

Strands SDK를 기반으로 구축된 Slidev 슬라이드 작성 및 검토 도우미 Agent입니다.

## 기능

- 슬라이드 콘텐츠 분석 (구조, 명확성, 기술적 정확성)
- AWS MCP 도구를 활용한 AWS 정보 검증
- 구조화된 검토 보고서 생성
- Slidev 형식 슬라이드 생성 및 개선
- 프로젝트 스크립트 통합 (create-slide.sh, export-all.sh)

## 설치

```bash
# 가상환경 생성 및 활성화
python -m venv .venv
source .venv/bin/activate  # macOS/Linux

# 의존성 설치
pip install -e .

# 개발 의존성 설치 (선택)
pip install -e ".[dev]"
```

## 환경 설정

```bash
# .env.example을 복사하여 .env 파일 생성
cp .env.example .env

# AWS Bedrock API 키 설정
export AWS_BEDROCK_API_KEY=your_bedrock_api_key

# 또는 AWS 자격 증명 설정
export AWS_ACCESS_KEY_ID=your_access_key
export AWS_SECRET_ACCESS_KEY=your_secret_key
export AWS_REGION=us-east-1
```

## 사용법

```python
from src.agent import SlideReviewAgent

# Agent 초기화 (기본값: Claude Haiku 4.5, us-east-1)
agent = SlideReviewAgent()

# 또는 커스텀 모델 사용
agent = SlideReviewAgent(
    model_id="global.anthropic.claude-haiku-4-5-20251001-v1:0",
    region_name="us-east-1",
)

# 슬라이드 검토
report = agent.review_slide("slides/my-presentation/slides.md")
print(report)

# 슬라이드 생성
agent.create_slide("20260107-docker-basics", "Docker 기초")
```

## 프로젝트 구조

```
slide-review-agent/
├── src/
│   ├── __init__.py
│   ├── agent.py              # 메인 Agent 클래스
│   ├── models/               # 데이터 모델
│   │   ├── slide.py
│   │   ├── analysis.py
│   │   └── report.py
│   └── components/           # 컴포넌트
│       ├── content_analyzer.py
│       ├── aws_validator.py
│       ├── report_generator.py
│       ├── slide_generator.py
│       ├── slidev_validator.py
│       └── script_executor.py
├── tests/                    # 테스트
├── pyproject.toml
└── README.md
```
