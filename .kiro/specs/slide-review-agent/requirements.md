# 슬라이드 검토 도우미 Agent 요구사항

## 소개

슬라이드 작성 및 검토를 지원하는 AI Agent입니다. Strands SDK를 사용하여 AWS 관련 MCP 도구를 활용하고, 슬라이드 콘텐츠의 품질을 검토하며 개선 제안을 제공합니다.

## 용어집

- **Slide_Review_Agent**: 슬라이드 작성 및 검토를 지원하는 AI Agent
- **Strands_SDK**: AI Agent 개발을 위한 SDK
- **AWS_MCP**: AWS 관련 기능을 제공하는 Model Context Protocol 서버
- **Slide_Content**: Markdown 형식의 슬라이드 콘텐츠
- **Review_Report**: 슬라이드 검토 결과 보고서

## 요구사항

### 요구사항 1: Agent 초기화 및 설정

**사용자 스토리**: 개발자로서 Strands SDK를 사용하여 슬라이드 검토 Agent를 초기화하고 싶습니다. 이를 통해 AWS 관련 도구를 활용할 수 있게 하려고 합니다.

#### 수용 기준

1. WHEN Agent가 초기화될 때, THE Slide_Review_Agent SHALL Strands SDK를 사용하여 설정되어야 함
2. WHEN Agent가 초기화될 때, THE Slide_Review_Agent SHALL AWS MCP 도구에 접근할 수 있어야 함
3. WHEN Agent가 초기화될 때, THE Slide_Review_Agent SHALL 기본 시스템 프롬프트를 로드해야 함

### 요구사항 2: 슬라이드 콘텐츠 분석

**사용자 스토리**: 사용자로서 작성한 슬라이드 콘텐츠를 Agent가 분석하여 구조, 명확성, 기술적 정확성을 평가받고 싶습니다.

#### 수용 기준

1. WHEN 슬라이드 콘텐츠가 제공될 때, THE Slide_Review_Agent SHALL 콘텐츠의 구조를 분석해야 함
2. WHEN 슬라이드 콘텐츠가 제공될 때, THE Slide_Review_Agent SHALL 각 슬라이드의 명확성을 평가해야 함
3. WHEN 슬라이드 콘텐츠가 제공될 때, THE Slide_Review_Agent SHALL 기술적 정확성을 검증해야 함
4. WHEN 기술 용어가 포함될 때, THE Slide_Review_Agent SHALL AWS MCP 도구를 사용하여 정보를 검증해야 함

### 요구사항 3: 검토 보고서 생성

**사용자 스토리**: 개발자로서 슬라이드 검토 결과를 구조화된 보고서 형식으로 받고 싶습니다. 이를 통해 개선 사항을 명확하게 파악할 수 있습니다.

#### 수용 기준

1. WHEN 분석이 완료될 때, THE Slide_Review_Agent SHALL 구조화된 Review_Report를 생성해야 함
2. WHEN Review_Report가 생성될 때, THE Slide_Review_Agent SHALL 강점(Strengths) 섹션을 포함해야 함
3. WHEN Review_Report가 생성될 때, THE Slide_Review_Agent SHALL 개선 사항(Improvements) 섹션을 포함해야 함
4. WHEN Review_Report가 생성될 때, THE Slide_Review_Agent SHALL 구체적인 제안(Suggestions) 섹션을 포함해야 함

### 요구사항 4: 개선 제안 생성

**사용자 스토리**: 사용자로서 슬라이드를 개선하기 위한 구체적인 제안을 받고 싶습니다. 이를 통해 슬라이드의 품질을 향상시킬 수 있습니다.

#### 수용 기준

1. WHEN 검토가 완료될 때, THE Slide_Review_Agent SHALL 우선순위가 지정된 개선 제안을 생성해야 함
2. WHEN 개선 제안이 생성될 때, THE Slide_Review_Agent SHALL 각 제안에 대한 이유를 설명해야 함
3. WHEN 개선 제안이 생성될 때, THE Slide_Review_Agent SHALL 구현 예시를 제공해야 함
4. WHERE 기술적 검증이 필요할 때, THE Slide_Review_Agent SHALL AWS MCP 도구를 활용하여 정보를 확인해야 함

### 요구사항 5: Slidev 기반 슬라이드 작성 지원

**사용자 스토리**: 개발자로서 Slidev 프레임워크를 사용하여 새로운 슬라이드를 작성할 때 Agent의 지원을 받고 싶습니다. 이를 통해 프로젝트 표준에 맞는 고품질의 슬라이드를 효율적으로 작성할 수 있습니다.

#### 수용 기준

1. WHEN 사용자가 슬라이드 작성을 요청할 때, THE Slide_Review_Agent SHALL Slidev 형식의 슬라이드 구조 템플릿을 제안해야 함
2. WHEN 슬라이드 주제가 제공될 때, THE Slide_Review_Agent SHALL 관련 AWS 정보를 MCP 도구로 검색하고 콘텐츠에 반영해야 함
3. WHEN Slidev 슬라이드 초안이 생성될 때, THE Slide_Review_Agent SHALL 프로젝트의 기존 슬라이드 스타일과 일관성을 검토해야 함
4. WHEN 초안 검토가 완료될 때, THE Slide_Review_Agent SHALL Slidev 형식을 유지하면서 개선된 버전을 제안해야 함
5. WHEN 슬라이드가 생성될 때, THE Slide_Review_Agent SHALL 프로젝트의 {yyyymmdd}-{title} 네이밍 컨벤션을 준수하도록 제안해야 함
6. WHEN 슬라이드 생성이 필요할 때, THE Slide_Review_Agent SHALL scripts/create-slide.sh 스크립트를 활용하여 슬라이드를 생성해야 함

### 요구사항 7: 프로젝트 스크립트 활용

**사용자 스토리**: 시스템 관리자로서 Agent가 프로젝트에 정의된 스크립트를 활용하여 슬라이드를 생성하고 관리하기를 원합니다. 이를 통해 프로젝트 표준을 일관되게 유지할 수 있습니다.

#### 수용 기준

1. WHEN 슬라이드 생성이 필요할 때, THE Slide_Review_Agent SHALL scripts/create-slide.sh를 호출해야 함
2. WHEN 슬라이드 내보내기가 필요할 때, THE Slide_Review_Agent SHALL scripts/export-all.sh를 활용할 수 있어야 함
3. WHEN 스크립트 실행 중 오류가 발생할 때, THE Slide_Review_Agent SHALL 오류를 처리하고 사용자에게 알려야 함
4. WHEN 스크립트가 성공적으로 실행될 때, THE Slide_Review_Agent SHALL 생성된 슬라이드에 대해 자동으로 검토를 수행해야 함

### 요구사항 6: 도구 통합

**사용자 스토리**: 시스템 아키텍트로서 Agent가 AWS MCP 도구를 효과적으로 활용하기를 원합니다. 이를 통해 정확한 AWS 정보를 기반으로 검토할 수 있습니다.

#### 수용 기준

1. WHEN Agent가 AWS 관련 정보가 필요할 때, THE Slide_Review_Agent SHALL AWS MCP 도구를 호출해야 함
2. WHEN MCP 도구 호출이 실패할 때, THE Slide_Review_Agent SHALL 오류를 처리하고 대체 방안을 제시해야 함
3. WHEN 도구 응답이 수신될 때, THE Slide_Review_Agent SHALL 응답을 분석하여 검토에 반영해야 함
4. WHEN 도구 호출 결과가 모순될 때, THE Slide_Review_Agent SHALL 사용자에게 알리고 확인을 요청해야 함
