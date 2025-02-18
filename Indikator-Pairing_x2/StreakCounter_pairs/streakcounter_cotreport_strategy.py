import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StreakCounter_COTReport_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StreakCounter und COTReport
    """
    
    params = (
        ('indicators', {
            'StreakCounter': {
                'class': StreakCounter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StreakCounter'>
            },
            'COTReport': {
                'class': COTReport,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_COTReport'>
            }
        }),
        ('weights', {
            'StreakCounter': 1.0,
            'COTReport': 1.0
        })
    )
