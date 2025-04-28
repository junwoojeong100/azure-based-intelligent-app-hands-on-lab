# Intelligent App Hands-on Lab

이 리포지토리는 Azure OpenAI, AutoGen, GitHub Copilot, Docker, AKS 등 최신 AI 및 클라우드 기술을 활용한 지능형 애플리케이션 실습을 단계별로 제공합니다.

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

1. Python 3.10+ 및 Docker Desktop 설치
2. `requirements.txt` 기반 패키지 설치
3. 각 노트북을 순서대로 실습
4. (선택) Azure 구독 및 OpenAI, AKS, ACR 리소스 준비

## GitHub Codespaces에서 실습하기

이 리포지토리는 GitHub Codespaces 환경에서 바로 실행할 수 있습니다. Codespaces를 사용하면 별도의 로컬 환경 설정 없이 웹 브라우저에서 주피터 노트북을 바로 실행하고 실습할 수 있습니다.

1. 이 리포지토리를 GitHub에서 엽니다.
2. [Code] 버튼을 클릭하고 [Codespaces] 탭에서 [Create codespace on main]을 선택합니다.
3. Codespaces 환경이 준비되면, VS Code 웹 또는 Jupyter 인터페이스에서 노트북(.ipynb) 파일을 실행하세요.
4. 필요한 경우 터미널에서 `pip install -r requirements.txt`로 패키지를 설치하세요.

---

## 참고 자료
- [Microsoft AutoGen 공식 문서](https://microsoft.github.io/autogen/)
- [Azure OpenAI Service](https://learn.microsoft.com/azure/cognitive-services/openai/)
- [Azure Kubernetes Service](https://learn.microsoft.com/azure/aks/)
- [GitHub Copilot](https://docs.github.com/en/copilot)

---

이 리포지토리는 교육 및 실습 목적이며, 실제 서비스 배포 시에는 보안 및 운영 환경을 추가로 고려해야 합니다.
