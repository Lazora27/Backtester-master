import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannFans_COTReport_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannFans und COTReport
    """
    
    params = (
        ('indicators', {
            'GannFans': {
                'class': GannFans,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannFans'>
            },
            'COTReport': {
                'class': COTReport,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_COTReport'>
            }
        }),
        ('weights', {
            'GannFans': 1.0,
            'COTReport': 1.0
        })
    )
