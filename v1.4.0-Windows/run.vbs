Set WshShell = CreateObject("WScript.Shell")
Set fso = CreateObject("Scripting.FileSystemObject")

' VBScript 파일이 위치한 폴더 경로 가져오기
currentFolder = fso.GetParentFolderName(WScript.ScriptFullName)

' run.bat 파일의 전체 경로 생성
batchFile = Chr(34) & fso.BuildPath(currentFolder, "run.bat") & Chr(34)

' 배치 파일을 숨긴 상태로 실행
WshShell.Run "cmd.exe /c " & batchFile, 0

' 객체 해제
Set WshShell = Nothing
Set fso = Nothing