
function CreateShortcut(target_path)
{
   wsh = new ActiveXObject('WScript.Shell');
   link = wsh.CreateShortcut(wsh.SpecialFolders("Startup") + '\\autobras.lnk');
   link.TargetPath = target_path;
   link.WindowStyle = 7;
   link.Description = 'AutoBras';
   link.WorkingDirectory = wsh.CurrentDirectory;
   link.Save();
}

function main()
{
   wsh = new ActiveXObject('WScript.Shell');
   fso = new ActiveXObject('Scripting.FileSystemObject');

   if(wsh.Popup('是否将autobras.bat加入到启动项？(本对话框6秒后消失)', 6, 'autobras 对话框', 1+32) == 1) {
       CreateShortcut('"' + wsh.CurrentDirectory + '\\autobras.bat"');
       wsh.Popup('成功加入autobras到启动项', 5, 'autobras 对话框', 64);
   }
}

main();
