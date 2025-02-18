import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DOMDepth_COTReport_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DOMDepth und COTReport
    """
    
    params = (
        ('indicators', {
            'DOMDepth': {
                'class': DOMDepth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DOMDepth'>
            },
            'COTReport': {
                'class': COTReport,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_COTReport'>
            }
        }),
        ('weights', {
            'DOMDepth': 1.0,
            'COTReport': 1.0
        })
    )
