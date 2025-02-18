import backtrader as bt
from ..base_strategy import FlexibleStrategy

class COTReport_TrueRangeIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von COTReport und TrueRangeIndicator
    """
    
    params = (
        ('indicators', {
            'COTReport': {
                'class': COTReport,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_COTReport'>
            },
            'TrueRangeIndicator': {
                'class': TrueRangeIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRangeIndicator'>
            }
        }),
        ('weights', {
            'COTReport': 1.0,
            'TrueRangeIndicator': 1.0
        })
    )
