import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrendExhaustion_COTReport_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrendExhaustion und COTReport
    """
    
    params = (
        ('indicators', {
            'TrendExhaustion': {
                'class': TrendExhaustion,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendExhaustion'>
            },
            'COTReport': {
                'class': COTReport,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_COTReport'>
            }
        }),
        ('weights', {
            'TrendExhaustion': 1.0,
            'COTReport': 1.0
        })
    )
