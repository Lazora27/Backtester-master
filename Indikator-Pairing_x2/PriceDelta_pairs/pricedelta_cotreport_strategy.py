import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceDelta_COTReport_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceDelta und COTReport
    """
    
    params = (
        ('indicators', {
            'PriceDelta': {
                'class': PriceDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceDelta'>
            },
            'COTReport': {
                'class': COTReport,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_COTReport'>
            }
        }),
        ('weights', {
            'PriceDelta': 1.0,
            'COTReport': 1.0
        })
    )
