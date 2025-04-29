# Intelligent App Hands-on Lab

이 리포지토리는 Azure OpenAI, AutoGen, GitHub Copilot, Docker, Azure Kubernetes Service 등 최신 AI 및 클라우드 기술을 활용한 지능형 애플리케이션 실습을 단계별로 제공합니다.

## 구성

- **1.LLM_PromptEngineering.ipynb**
  - LLM(대형 언어 모델)과 프롬프트 엔지니어링의 기본 개념 및 실습
  - Azure OpenAI API 활용 예제

- **2.GitHubCopilot_AutoGen.ipynb**
  - GitHub Copilot Agent Mode와 AutoGen 프레임워크를 활용한 멀티 에이전트 앱 구현
  - 여행 플래너 Multi-Agent 예제 실습

- **3.Container_ACR_AKS.ipynb**
  - 여행 플래너 앱을 Docker 컨테이너로 빌드
  - Azure Container Registry(ACR) 및 Azure Kubernetes Service(AKS)로 배포
  - Log Analytics를 통한 컨테이너 로그 조회

- **requirements.txt**
  - 실습에 필요한 주요 파이썬 패키지 목록

## 실습 주요 흐름

1. **LLM 및 프롬프트 엔지니어링**
   - LLM의 원리와 프롬프트 설계법 실습
   - Azure OpenAI API 엔드포인트 활용

2. **멀티 에이전트 앱 개발**
   - AutoGen 기반 여행 플래너 Multi-Agent 시스템 구현
   - 다양한 역할의 AI 에이전트 협업 구조 설계

3. **컨테이너화 및 클라우드 배포**
   - Dockerfile 작성 및 이미지 빌드
   - ACR/AKS를 통한 클라우드 배포
   - Log Analytics로 운영 로그 모니터링

## 빠른 시작

1. Azure 구독 및 Azure OpenAI, AKS, ACR 리소스 준비
2. GitHub Codespaces 환경 생성
3. Azure OpenAI 환경변수 설정
4. 각 노트북을 순서대로 실습

## GitHub Codespaces 환경 생성

GitHub Codespaces는 GitHub에서 제공하는 클라우드 기반 개발 환경으로, 별도의 로컬 설치 없이 웹 브라우저에서 바로 개발과 실습이 가능합니다. Codespaces 환경에는 이미 git, docker, kubectl, helm, python, pip, curl, wget 등 주요 개발 및 DevOps 도구가 사전 설치되어 있어, 추가 설치 없이 바로 실습을 시작할 수 있습니다.

이 리포지토리는 GitHub Codespaces 환경에서 바로 실행할 수 있습니다. Codespaces를 사용하면 별도의 로컬 환경 설정 없이 웹 브라우저에서 주피터 노트북을 바로 실행하고 실습할 수 있습니다.

1. 이 리포지토리를 GitHub에서 엽니다.
2. [Code] 버튼을 클릭하고 [Codespaces] 탭에서 [Create codespace on main]을 선택합니다.
3. Codespaces 환경이 준비되면, 다음 안내에 따라, 필요한 확장 프로그램과 Python 커널을 선택합니다.
4. **노트북 실행 전, Codespaces의 안내에 따라 'Python'과 'Jupyter' 확장 프로그램을 설치하세요.**
5. **상단의 [Select Kernel] 버튼을 클릭해 Python 3.x 커널을 선택하세요.**

- [GitHub Codespaces Quickstart 공식 문서](https://docs.github.com/en/codespaces/getting-started/quickstart)

## Azure OpenAI 환경변수 설정

실습을 위해 아래와 같이 `.env` 파일을 생성하고, 본인의 Azure OpenAI 서비스 정보로 값을 입력하세요.

```
AZURE_OPENAI_ENDPOINT=
AZURE_OPENAI_API_KEY=
AZURE_OPENAI_API_VERSION=
AZURE_OPENAI_DEPLOYMENT_NAME=
```

- 위 값들은 Azure Portal에서 본인 구독의 OpenAI 리소스 정보를 참고하여 입력해야 합니다.
- `.env` 파일은 리포지토리 루트(최상위 폴더)에 위치해야 하며, 절대 민감 정보(키 등)를 외부에 공개하지 마세요.

### Azure OpenAI 리소스 생성 방법 (간단 안내)

1. [Azure Portal](https://portal.azure.com/)에 로그인합니다.
2. "리소스 만들기"에서 "Azure OpenAI"를 검색해 리소스를 생성합니다.
3. 리소스 내에서 "키 및 엔드포인트" 메뉴에서 엔드포인트와 API 키를 확인합니다.
4. "모델 배포" 메뉴에서 원하는 모델(gpt-4o 등)을 배포하고, 배포 이름을 확인합니다.
5. 위 정보를 `.env` 파일에 입력합니다.

자세한 내용은 [Azure OpenAI Service Quickstart](https://learn.microsoft.com/en-us/azure/ai-services/openai/chatgpt-quickstart?tabs=keyless%2Ctypescript-keyless%2Cpython-new%2Ccommand-line&pivots=programming-language-python)도 참고하세요.

---

## 참고 자료
- [Microsoft AutoGen](https://microsoft.github.io/autogen/)
- [Azure OpenAI Service](https://learn.microsoft.com/azure/cognitive-services/openai/)
- [Azure Kubernetes Service](https://learn.microsoft.com/azure/aks/)
- [GitHub Copilot](https://docs.github.com/en/copilot)
- [GitHub Codespaces](https://docs.github.com/en/codespaces)
---

이 리포지토리는 교육 및 실습 목적이며, 실제 서비스 배포 시에는 보안 및 운영 환경을 추가로 고려해야 합니다.
