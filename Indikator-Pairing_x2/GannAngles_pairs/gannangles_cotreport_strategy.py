import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannAngles_COTReport_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannAngles und COTReport
    """
    
    params = (
        ('indicators', {
            'GannAngles': {
                'class': GannAngles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannAngles1'>
            },
            'COTReport': {
                'class': COTReport,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_COTReport'>
            }
        }),
        ('weights', {
            'GannAngles': 1.0,
            'COTReport': 1.0
        })
    )
