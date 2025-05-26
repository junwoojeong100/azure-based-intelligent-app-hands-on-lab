# Azure-based Intelligent App Hands-on Lab

> **지능형 앱(인텔리전트 앱)이란?**
> 인공지능(AI)과 클라우드 기술을 활용해, 사용자의 입력·상황·데이터를 실시간으로 분석하고, 맞춤형 추천·자동화·의사결정 지원 등 고도화된 기능을 제공하는 소프트웨어를 의미합니다. 대표적으로 LLM(대형 언어 모델), 자연어 처리, 예측 분석, 멀티모달 처리, 에이전트 기반 자동화 등이 포함됩니다.

이 리포지토리는 Azure OpenAI, AutoGen, GitHub Copilot, Docker, Azure Kubernetes Service, Azure AI Search 등 최신 AI 및 클라우드 기술을 활용한 지능형 애플리케이션 실습을 단계별로 제공합니다.

## 구성

- **README.md**
  - 실습 전체의 흐름, 환경 준비, 단계별 실습 방법, 주요 파일 안내 등 전반적인 가이드 역할을 하는 문서입니다.
  - 실습 시작 전 반드시 읽고, 안내에 따라 환경을 설정하세요.

- **.env**
  - Azure OpenAI 연동을 위한 엔드포인트, API 키 등 환경 변수 정보를 담는 파일입니다.
  - 민감 정보가 포함되므로 외부에 노출되지 않도록 주의하세요.

- **requirements.txt**
  - 실습에 필요한 주요 파이썬 패키지 목록이 정리되어 있습니다.

- **01-getting-started-with-prompt-engineering-for-llm.ipynb**
  - LLM(대형 언어 모델)과 프롬프트 엔지니어링의 기본 개념 및 실습을 다룹니다.
  - Azure OpenAI API 활용 예제를 포함합니다.

- **02-building-autogen-app-with-github-copilot.ipynb**
  - GitHub Copilot Agent Mode와 AutoGen 프레임워크를 활용한 멀티 에이전트 앱 구현 실습입니다.
  - 여행 플래너 Multi-Agent 예제를 다룹니다.


- **03-deploying-to-aks-using-docker-and-acr.ipynb**
  - 여행 플래너 앱을 Docker 컨테이너로 빌드하고, Azure Container Registry(ACR) 및 Azure Kubernetes Service(AKS)로 배포하는 과정을 실습합니다.
  - Log Analytics를 통한 컨테이너 로그 조회 방법도 포함되어 있습니다.

- **04-rag-with-azure-ai-search-and-openai.ipynb**
  - RAG(검색 증강 생성, Retrieval Augmented Generation)의 필요성과 개념을 설명합니다.
  - Azure Blob Storage, AI Search, OpenAI를 활용한 RAG 파이프라인(데이터 업로드, 인덱싱, 임베딩, 벡터 검색, LLM 답변 생성) 실습을 단계별로 제공합니다.

- **travel_planning_agent.py**
  - 여행 플래너 Multi-Agent의 핵심 로직이 구현된 파이썬 소스 파일입니다.
  - 에이전트 간 상호작용 및 여행 일정 추천 기능을 담당합니다.

---
## 빠른 시작

1. Azure 구독 준비
2. GitHub Codespaces 환경 생성 (아래 'GitHub Codespaces 환경 생성' 섹션 참고)
3. Azure OpenAI 환경변수 설정 (아래 'Azure OpenAI 환경변수 설정' 섹션 참고)
4. 각 노트북을 순서대로 실습


## 필수 계정 및 권한 요약

- **GitHub 계정**: 모든 실습에 필요하며, Codespaces 사용을 위해 반드시 필요합니다. 
- **Azure 계정**: 구독(Subscription) 또는 리소스 그룹(Resource Group)에 '기여자(Contributor)' 역할만 있으면 모든 실습(리소스 생성, 배포, 관리 등)이 가능합니다. Owner(소유자) 권한은 필요하지 않습니다.
  - Contributor는 리소스 생성/수정/삭제/배포/키 조회가 가능하며, 권한 부여/회수는 불가합니다.

> [Azure Built-in 역할 설명: Contributor, Owner 등](https://learn.microsoft.com/azure/role-based-access-control/built-in-roles) / [RBAC 개요](https://learn.microsoft.com/azure/role-based-access-control/overview)


## GitHub Codespaces 환경 생성

GitHub Codespaces는 GitHub에서 제공하는 클라우드 기반 개발 환경으로, 별도의 로컬 설치 없이 웹 브라우저에서 바로 개발과 실습이 가능합니다. Codespaces 환경에는 이미 git, docker, kubectl, helm, python, pip, curl, wget 등 주요 개발 및 DevOps 도구가 사전 설치되어 있어, 추가 설치 없이 바로 실습을 시작할 수 있습니다.

이 리포지토리는 GitHub Codespaces 환경에서 바로 실행할 수 있습니다. Codespaces를 사용하면 별도의 로컬 환경 설정 없이 웹 브라우저에서 주피터 노트북을 바로 실행하고 실습할 수 있습니다.

1. 이 리포지토리를 GitHub에서 엽니다.
2. [Code] 버튼을 클릭하고 [Codespaces] 탭에서 [Create codespace on master]를 선택합니다.
3. Codespaces 환경이 준비되면, 필요한 확장 프로그램과 Python 커널을 선택합니다.
4. **노트북 실행 전, Codespaces의 안내에 따라 'Python'과 'Jupyter' 확장 프로그램을 설치합니다.**
5. **상단의 [Select Kernel] 버튼을 클릭해 Python 3.x 커널을 선택합니다.**
6. **Python 가상환경(venv)을 생성합니다.**
   - 메뉴를 통해 생성: VS Code/Codespaces에서 Python 버전 표시줄을 클릭 → [Python: Create Environment] 또는 [가상 환경 생성] 메뉴를 선택 → venv를 선택하고 위치를 지정합니다. 생성된 가상환경을 커널로 선택합니다.
   - 또는 터미널에서 아래 명령어로 생성할 수 있습니다:
     ```bash
     python3 -m venv .venv
     source .venv/bin/activate
     ```
   - 가상환경을 생성한 후, [Select Kernel]에서 해당 venv를 선택해 사용합니다.

자세한 내용은 [GitHub Codespaces Quickstart](https://docs.github.com/en/codespaces/getting-started/quickstart)을 참고하세요.

## Azure OpenAI 환경변수 설정

실습을 위해 아래와 같이 `.env` 파일을 생성하고, 본인의 Azure OpenAI 서비스 정보로 값을 입력하세요.

```
AZURE_OPENAI_ENDPOINT=
AZURE_OPENAI_API_KEY=
AZURE_OPENAI_API_VERSION=
AZURE_OPENAI_DEPLOYMENT_NAME=
AZURE_OPENAI_EMBEDDING_DEPLOYMENT_NAME=
```

- 위 값들은 Azure Portal에서 본인 구독의 OpenAI 리소스 정보를 참고하여 입력해야 합니다.
- `.env` 파일은 리포지토리 루트(최상위 폴더)에 위치해야 하며, 절대 민감 정보(키 등)를 외부에 공개하지 마세요.

### Azure OpenAI 리소스 생성 및 gpt-4.1-mini 모델 배포 방법 (요약)

1. [Azure Portal](https://portal.azure.com/)에 로그인합니다.
2. "리소스 만들기"에서 "Azure AI Foundry"를 검색해 리소스를 생성합니다.
3. 리소스 내에서 "모델" 메뉴로 이동하여 **gpt-4.1-mini** 모델을 선택합니다.
4. "배포" 버튼을 클릭하여 모델을 배포하고, 배포 이름을 지정합니다.
5. 동일한 방식으로 "모델" 메뉴에서 **text-embedding-3-large** 모델을 선택하여 배포하고, 배포 이름을 지정합니다.
6. "엔드포인트 및 키" 메뉴에서 엔드포인트와 API 키를 확인합니다.
7. 위 정보를 `.env` 파일에 입력합니다.

> **참고:**
> - `gpt-4.1-mini`는 생성형 AI 용도로, `text-embedding-3-large`는 임베딩(문서 벡터화) 용도로 각각 배포해야 합니다.
> - 두 모델 모두 배포 후, 배포 이름을 `.env` 파일의 `AZURE_OPENAI_DEPLOYMENT_NAME`(gpt-4.1-mini)와 `AZURE_OPENAI_EMBEDDING_DEPLOYMENT`(text-embedding-3-large)로 구분해 입력하세요.


#### GPT-4.1 mini 모델 특장점
- **경량화**: 기존 GPT-4 계열 및 GPT-4o mini 대비 더욱 가볍고 빠른 응답 속도를 제공합니다.
- **비용 효율성**: GPT-4o mini 대비 더 낮은 비용으로 높은 성능을 발휘해 실습, 프로토타이핑, 실제 서비스에도 적합합니다.
- **성능 향상**: GPT-4o mini 대비 향상된 처리 속도와 응답 품질을 제공합니다.
- **멀티모달 지원**: 텍스트, 이미지 등 다양한 입력을 효율적으로 처리할 수 있습니다.
- **최신 아키텍처**: 최신 GPT-4.1 기반의 아키텍처로, 자연스러운 대화와 다양한 태스크에 강점을 가집니다.
  - **OpenAI 모델별 가격 정보는 [OpenAI 공식 가격 안내](https://platform.openai.com/docs/pricing)에서 확인할 수 있습니다.** (모델별 비용, 과금 방식 등 최신 정보 제공)
  - **OpenAI에서 제공하는 모든 모델의 상세 정보는 [OpenAI 모델 공식 문서](https://platform.openai.com/docs/models)에서 확인할 수 있습니다.** (모델별 기능, 지원 입력/출력, 용도 등 최신 정보 제공)

#### text-embedding-3-large 모델 특장점
- **최신 임베딩 품질**: OpenAI의 최신 임베딩 모델로, 의미적 유사성, 검색, 분류, 클러스터링 등 다양한 태스크에서 뛰어난 성능을 보입니다.
- **고차원 벡터 지원**: 3,072차원의 고차원 벡터를 생성하여, 대규모 문서/문장 검색 및 추천 시스템에 적합합니다.
- **다국어 지원**: 한국어, 영어 등 다양한 언어의 텍스트 임베딩을 효과적으로 지원합니다.
- **비용 효율성**: 기존 text-embedding-ada-002 대비 더 높은 품질과 효율성을 제공합니다.
- **확장성**: 대용량 데이터셋, 벡터 DB, Azure AI Search 등과 연동해 대규모 검색/분석 시스템 구축에 적합합니다.
  - **OpenAI 임베딩 모델별 가격 정보는 [OpenAI 공식 가격 안내](https://platform.openai.com/docs/pricing/embeddings)에서 확인할 수 있습니다.**
  - **임베딩 모델 상세 정보는 [OpenAI 임베딩 공식 문서](https://platform.openai.com/docs/guides/embeddings)에서 확인할 수 있습니다.**

자세한 내용은 [Azure AI Foundry에서 OpenAI 모델 배포 가이드](https://learn.microsoft.com/ko-kr/azure/ai-foundry/how-to/deploy-models-openai)를 참고하세요.

---

## 참고 자료
- [GitHub Codespaces](https://docs.github.com/en/codespaces)
- [Azure AI Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/)
- [Azure OpenAI Service](https://learn.microsoft.com/azure/cognitive-services/openai/)
- [GitHub Copilot](https://docs.github.com/en/copilot)
- [Microsoft AutoGen](https://microsoft.github.io/autogen/)
- [Azure Kubernetes Service](https://learn.microsoft.com/azure/aks/)
- [Azure Blob Storage](https://learn.microsoft.com/azure/storage/blobs/)
- [Azure AI Search](https://learn.microsoft.com/azure/search/)
---

이 리포지토리는 교육 및 실습 목적이며, 실제 서비스 배포 시에는 보안 및 운영 환경을 추가로 고려해야 합니다.
