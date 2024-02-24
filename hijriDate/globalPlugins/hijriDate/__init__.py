from . import hijri_converter
import api
import wx
import gui
import globalPluginHandler
import ui
from scriptHandler import script
import addonHandler
addonHandler.initTranslation()

class GlobalPlugin(globalPluginHandler.GlobalPlugin):
	scriptCategory= _("hijri date")
	@script(gesture="kb:NVDA+h")
	def script_toggle(self,gesture):
		hijriDate=str(hijri_converter.Hijri.today()).split("-")
		hijri={"1": _("Muharram"),"2": _("Safar"),"3": _("Rabi' al-awwal"),"4": _("Rabi' al-thani"),"5": _("Jumada al-awwal"),"6": _("Jumada al-thani"),"7": _("Rajab"),"8": _("Sha'ban"),"9": _("Ramadan"),"10": _("Shawwal"),"11": _("Dhu al-Qi'dah"),"12": _("Dhu al-Hijjah")}
		if hijriDate[1].startswith("0"):
			hijriDate[1]=hijriDate[1][1]
		ui.message("{} {} {}".format(hijriDate[2],hijri[hijriDate[1]],hijriDate[0]))
	script_toggle.__doc__= _("say current hijri date")

