# Git-Practice

### [About gitignore]

.gitignore : 버전 관리를 진행할 때 원격 저장소에 따로 올리고 싶지 않은 목록을 관리할 때 사용한다.

https://www.toptal.com/developers/gitignore/

----

### [Conventional Commits]

1. commit의 제목은 commit을 설명하는 하나의 구나 절로 완성한다
2. 띄어쓰기와 대문자 처리를 잘 해준다. ex) Importance of Capitalize
3. Prefix 꼭 달기
  - feat : 기능 개발 관련
  - fix : 오류 개선 혹은 버그 패치
  - docs : 문서화 작업
  - test : 테스트 관련
  - conf : 환경설정 관련
  - build : 빌드 관련
  - ci : Continuous Integration 관련

## Documentation Management in README 

### Installation

```shell
$ git clone {repo url}
$ cd {reponame}
$ pip install ...
```

### How To Start

```shell
$ python main.py
```

### Dependency

- Python : 3.10 ver