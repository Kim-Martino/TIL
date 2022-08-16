<h1> 22-08-16 git bash command </h1> 


<b> git bash 명령어 </b>

- cd : 디렉토리 위치를 변경한다. 
- ls : 해당 디렉토리에 존재하는 파일, 디렉토리를 모두 불러온다.
- cd .. : 상위 파일로 이동한다.
- rm : 파일을 삭제한다.
- mv : 파일을 이동시키거나 파일명을 변경한다.
- vi/vim : 파일 편집기를 실행시킨다.
- cat : 파일의 내용을 출력한다.

<b> vim 명령어 </b>
- :w : 편집한 파일을 저장한다
- :q : vim 상태에서 빠져나온다.
- :wq : 파일을 저장한 후 종료한다.

<b> git 설치 </b>

		환경설정
- git config --global user.name "GitHubName"
- git config --global user.email "EmailAddress"
- git config --global core.editor "vim"
- git config --global core.page "cat"


- git config --global alias.lg "log --color --graph --
pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr)
%C(bold blue)<%an>%Creset' --abbrev-commit"

		설정확인
- git config --list 

<b> git 명령어 </b>

- git clone [repository address] : 자신의 GitHub 저장소에 접근한다.
- git add File_Name : Commit 할 파일을 staged 상태로 전환한다.
- git commit File_Name : 파일을 Commit한다. 이때 변경된 내용을 삽입하여
			 어떤 점이 바뀌었는지 적어준다.
- git push origin main : Commit한 파일을 GitHub에 Update한다.


<b> commit 문법 </b>
- feat : 기능 개발 관련
- fix : 오류 개선 혹 버그 패치
- docs : 문서화 작업
- test : test 관련
- conf : 환경설정 관련
- build : 빌드 관련


