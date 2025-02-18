import backtrader as bt
from ..base_strategy import FlexibleStrategy

class COTReport_AutoHarmonicPattern_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von COTReport und AutoHarmonicPattern
    """
    
    params = (
        ('indicators', {
            'COTReport': {
                'class': COTReport,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_COTReport'>
            },
            'AutoHarmonicPattern': {
                'class': AutoHarmonicPattern,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoHarmonicPattern'>
            }
        }),
        ('weights', {
            'COTReport': 1.0,
            'AutoHarmonicPattern': 1.0
        })
    )
