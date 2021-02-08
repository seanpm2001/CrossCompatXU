Get-ChildItem -Path C:\ -Include *.exe,*.msi -File -Recurse -ErrorAction SilentlyContinue
New-Item -Path 'D:\temp\CrossCompatXU\Logs\ProgramList.txt' -ItemType File
Start-Sleep -Seconds 90
End
