import backtrader as bt
from ..base_strategy import FlexibleStrategy

class COTReport_SuperTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von COTReport und SuperTrend
    """
    
    params = (
        ('indicators', {
            'COTReport': {
                'class': COTReport,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_COTReport'>
            },
            'SuperTrend': {
                'class': SuperTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperTrend'>
            }
        }),
        ('weights', {
            'COTReport': 1.0,
            'SuperTrend': 1.0
        })
    )
