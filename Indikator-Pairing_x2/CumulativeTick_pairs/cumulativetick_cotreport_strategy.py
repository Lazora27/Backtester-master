import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CumulativeTick_COTReport_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CumulativeTick und COTReport
    """
    
    params = (
        ('indicators', {
            'CumulativeTick': {
                'class': CumulativeTick,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CumulativeTick'>
            },
            'COTReport': {
                'class': COTReport,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_COTReport'>
            }
        }),
        ('weights', {
            'CumulativeTick': 1.0,
            'COTReport': 1.0
        })
    )
