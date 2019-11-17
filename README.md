# PythonPrograms
atcoderのサンプルケースで自動で正誤判定して,それらが全問正解の場合,自動でコードを提出します.

<使用方法>

sel.pyでchromeを起動.

callc.pyでmain.cppで自動compile&run,自動判定を行います。全てのサンプルケースで正解した場合,自動的に提出を行います.

callp.pyでmain.pyで上と同様の事をします.

キードードショートカットとこれらのpythonファイルの併用を想定しています.

<例>

正誤判定用の時.

gnome-terminal -- bash -c "cd test;python callc.py;sleep 7;exit;bash"
