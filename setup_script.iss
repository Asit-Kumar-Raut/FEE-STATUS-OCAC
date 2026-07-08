; Inno Setup Script to compile FeeManager into a Setup Installer Wizard

[Setup]
AppName=College Fee Status Management
AppVersion=1.0.0
DefaultDirName={commonpf}\CollegeFeeStatusManagement
DefaultGroupName=College Fee Status Management
OutputDir=dist
OutputBaseFilename=FeeManagerSetup
Compression=lzma
SolidCompression=yes
DisableProgramGroupPage=yes

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Tasks]
Name: "desktopicon"; Description: "Create a &desktop shortcut"; GroupDescription: "Additional shortcuts:"; Flags: unchecked

[Files]
; Packages the compiled executable
Source: "dist\FeeManager\FeeManager.exe"; DestDir: "{app}"; Flags: ignoreversion
; Packages all dependent DLLs, system libraries, assets, and credentials
Source: "dist\FeeManager\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs

[Icons]
Name: "{group}\College Fee Status Management"; Filename: "{app}\FeeManager.exe"
Name: "{commondesktop}\College Fee Status Management"; Filename: "{app}\FeeManager.exe"; Tasks: desktopicon

[Run]
Filename: "{app}\FeeManager.exe"; Description: "Launch College Fee Status Management"; Flags: nowait postinstall skipifsilent
