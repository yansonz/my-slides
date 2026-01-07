# 슬라이드 검토 도우미 Agent 설계

## 개요

Strands SDK를 기반으로 구축된 슬라이드 검토 도우미 Agent입니다. AWS MCP 도구를 활용하여 AWS 관련 정보를 검증하고, Slidev 형식의 슬라이드 작성 및 검토를 지원합니다. 프로젝트의 스크립트와 통합되어 일관된 슬라이드 관리를 제공합니다.

## 아키텍처

```
┌─────────────────────────────────────────────────────────────┐
│                    Slide Review Agent                        │
│                   (Strands SDK 기반)                         │
└─────────────────────────────────────────────────────────────┘
                              │
                ┌─────────────┼─────────────┐
                │             │             │
        ┌───────▼────────┐   │   ┌─────────▼────────┐
        │  Content       │   │   │  AWS MCP Tools   │
        │  Analyzer      │   │   │  - Documentation │
        │                │   │   │  - Regional Info │
        └────────────────┘   │   │  - Search        │
                             │   └──────────────────┘
                    ┌────────▼────────┐
                    │  Report         │
                    │  Generator      │
                    └─────────────────┘
                             │
                ┌────────────┼────────────┐
                │            │            │
        ┌───────▼──────┐    │   ┌────────▼──────┐
        │ Script       │    │   │ Suggestion    │
        │ Executor     │    │   │ Generator     │
        │ (create-     │    │   │               │
        │  slide.sh)   │    │   └───────────────┘
        └──────────────┘    │
                    ┌───────▼────────┐
                    │ Slidev Format  │
                    │ Validator      │
                    └────────────────┘
```

## 컴포넌트 및 인터페이스

### 1. Agent 초기화 모듈 (AgentInitializer)

**책임**: Strands SDK를 사용하여 Agent를 초기화하고 AWS MCP 도구를 연결

**인터페이스**:
```typescript
interface AgentInitializer {
  initializeAgent(): Promise<Agent>
  loadSystemPrompt(): string
  connectAWSTools(): Promise<void>
}
```

**주요 기능**:
- Strands SDK 설정
- AWS MCP 도구 연결
- 시스템 프롬프트 로드

### 2. 콘텐츠 분석기 (ContentAnalyzer)

**책임**: 슬라이드 콘텐츠의 구조, 명확성, 기술적 정확성 분석

**인터페이스**:
```typescript
interface ContentAnalyzer {
  analyzeStructure(content: string): StructureAnalysis
  evaluateClarity(content: string): ClarityScore
  validateTechnicalAccuracy(content: string): TechnicalValidation
}
```

**주요 기능**:
- 슬라이드 구조 분석
- 명확성 평가
- 기술 용어 검증

### 3. AWS 정보 검증기 (AWSInfoValidator)

**책임**: AWS MCP 도구를 사용하여 AWS 관련 정보 검증

**인터페이스**:
```typescript
interface AWSInfoValidator {
  searchDocumentation(query: string): Promise<SearchResult[]>
  getRegionalAvailability(service: string): Promise<RegionalInfo>
  validateAWSConcepts(concepts: string[]): Promise<ValidationResult>
}
```

**주요 기능**:
- AWS 문서 검색
- 지역별 가용성 확인
- AWS 개념 검증

### 4. 보고서 생성기 (ReportGenerator)

**책임**: 구조화된 검토 보고서 생성

**인터페이스**:
```typescript
interface ReportGenerator {
  generateReport(analysis: Analysis): ReviewReport
  formatReport(report: ReviewReport): string
}

interface ReviewReport {
  strengths: string[]
  improvements: string[]
  suggestions: Suggestion[]
  overallScore: number
}

interface Suggestion {
  priority: 'high' | 'medium' | 'low'
  description: string
  reason: string
  example: string
}
```

**주요 기능**:
- 강점 식별
- 개선 사항 도출
- 우선순위 지정 제안

### 5. 슬라이드 생성기 (SlideGenerator)

**책임**: Slidev 형식의 슬라이드 생성 및 개선

**인터페이스**:
```typescript
interface SlideGenerator {
  generateTemplate(topic: string): string
  generateContent(topic: string, awsContext: string): string
  improveSlide(content: string): string
}
```

**주요 기능**:
- Slidev 템플릿 생성
- AWS 정보 기반 콘텐츠 생성
- 슬라이드 개선

### 6. 스크립트 실행기 (ScriptExecutor)

**책임**: 프로젝트 스크립트 실행 및 오류 처리

**인터페이스**:
```typescript
interface ScriptExecutor {
  executeCreateSlide(slideName: string): Promise<ExecutionResult>
  executeExportAll(): Promise<ExecutionResult>
  handleScriptError(error: Error): void
}
```

**주요 기능**:
- create-slide.sh 실행
- export-all.sh 실행
- 오류 처리 및 보고

### 7. Slidev 형식 검증기 (SlidevValidator)

**책임**: Slidev 형식 준수 여부 검증

**인터페이스**:
```typescript
interface SlidevValidator {
  validateFormat(content: string): ValidationResult
  checkConsistency(content: string, existingSlides: string[]): ConsistencyReport
  validateNamingConvention(slideName: string): boolean
}
```

**주요 기능**:
- Slidev 형식 검증
- 스타일 일관성 확인
- 네이밍 컨벤션 검증

## 데이터 모델

### SlideContent
```typescript
interface SlideContent {
  title: string
  topic: string
  slides: Slide[]
  metadata: {
    author: string
    date: string
    theme: string
  }
}

interface Slide {
  title: string
  content: string
  notes?: string
  layout?: string
}
```

### Analysis
```typescript
interface Analysis {
  structure: StructureAnalysis
  clarity: ClarityScore
  technicalAccuracy: TechnicalValidation
  awsValidation: ValidationResult
  slidevCompliance: ValidationResult
}

interface StructureAnalysis {
  slideCount: number
  hasIntroduction: boolean
  hasConclusion: boolean
  logicalFlow: number // 0-100
}

interface ClarityScore {
  overallScore: number // 0-100
  issues: ClarityIssue[]
}

interface ClarityIssue {
  slideIndex: number
  issue: string
  suggestion: string
}

interface TechnicalValidation {
  isValid: boolean
  errors: string[]
  warnings: string[]
}

interface ValidationResult {
  isValid: boolean
  details: string[]
}
```

### ExecutionResult
```typescript
interface ExecutionResult {
  success: boolean
  output: string
  error?: string
  slidePath?: string
}
```

## 오류 처리

### 오류 유형

1. **AWS MCP 도구 오류**
   - 도구 호출 실패 시 대체 방안 제시
   - 사용자에게 알림

2. **스크립트 실행 오류**
   - 스크립트 실패 시 오류 메시지 표시
   - 수동 개입 제안

3. **형식 검증 오류**
   - Slidev 형식 오류 시 수정 제안
   - 네이밍 컨벤션 위반 시 올바른 형식 제시

4. **콘텐츠 분석 오류**
   - 분석 실패 시 부분 결과 반환
   - 사용자에게 재시도 제안

## 테스트 전략

### 단위 테스트
- 각 컴포넌트의 개별 기능 테스트
- 입력 검증 및 출력 형식 확인
- 오류 처리 로직 검증

### 통합 테스트
- Agent 초기화 및 AWS 도구 연결
- 전체 분석 파이프라인
- 스크립트 실행 및 결과 처리

### 속성 기반 테스트
- 보고서 생성의 일관성
- 슬라이드 형식 검증의 정확성
- 제안 생성의 품질

## 정정 속성(Correctness Properties)

속성(Property)은 시스템이 모든 유효한 실행에서 참이어야 하는 특성입니다. 속성은 인간이 읽을 수 있는 사양과 기계가 검증 가능한 정확성 보장 사이의 다리 역할을 합니다.

### Property 1: 보고서 구조 일관성
*모든* 슬라이드 콘텐츠에 대해, 생성된 보고서는 항상 Strengths, Improvements, Suggestions 섹션을 포함해야 함
**Validates: Requirements 3.2, 3.3, 3.4**

### Property 2: AWS 정보 검증 라운드 트립
*모든* AWS 관련 용어에 대해, AWS MCP 도구로 검색한 후 반환된 정보는 원본 쿼리와 의미적으로 일치해야 함
**Validates: Requirements 2.4, 6.1**

### Property 3: Slidev 형식 보존
*모든* 슬라이드 생성 및 개선 작업에 대해, 출력 콘텐츠는 유효한 Slidev 형식을 유지해야 함
**Validates: Requirements 5.1, 5.4**

### Property 4: 네이밍 컨벤션 준수
*모든* 생성된 슬라이드에 대해, 폴더명은 {yyyymmdd}-{title} 형식을 따라야 함
**Validates: Requirements 5.5**

### Property 5: 스크립트 실행 원자성
*모든* 스크립트 실행에 대해, 성공하면 완전한 슬라이드 구조가 생성되어야 하고, 실패하면 부분적 상태가 남지 않아야 함
**Validates: Requirements 5.6, 7.1**

### Property 6: 분석 결과 완전성
*모든* 슬라이드 콘텐츠에 대해, 분석 결과는 구조, 명확성, 기술적 정확성, AWS 검증을 모두 포함해야 함
**Validates: Requirements 2.1, 2.2, 2.3, 2.4**

### Property 7: 제안 우선순위 일관성
*모든* 생성된 제안에 대해, 우선순위가 높을수록 영향도가 커야 하고, 같은 우선순위 내에서는 일관된 순서를 유지해야 함
**Validates: Requirements 4.1**

### Property 8: 오류 처리 복원력
*모든* 오류 상황에 대해, Agent는 오류를 처리하고 사용자에게 명확한 메시지를 제공해야 하며, 부분적 결과를 반환할 수 있어야 함
**Validates: Requirements 6.2, 6.4, 7.3**
