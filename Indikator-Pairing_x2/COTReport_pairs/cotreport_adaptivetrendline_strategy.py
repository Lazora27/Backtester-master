import backtrader as bt
from ..base_strategy import FlexibleStrategy

class COTReport_AdaptiveTrendLine_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von COTReport und AdaptiveTrendLine
    """
    
    params = (
        ('indicators', {
            'COTReport': {
                'class': COTReport,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_COTReport'>
            },
            'AdaptiveTrendLine': {
                'class': AdaptiveTrendLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveTrendLine'>
            }
        }),
        ('weights', {
            'COTReport': 1.0,
            'AdaptiveTrendLine': 1.0
        })
    )
