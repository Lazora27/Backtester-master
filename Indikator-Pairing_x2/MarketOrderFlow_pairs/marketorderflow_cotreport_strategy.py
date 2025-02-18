import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketOrderFlow_COTReport_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketOrderFlow und COTReport
    """
    
    params = (
        ('indicators', {
            'MarketOrderFlow': {
                'class': MarketOrderFlow,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketOrderFlow'>
            },
            'COTReport': {
                'class': COTReport,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_COTReport'>
            }
        }),
        ('weights', {
            'MarketOrderFlow': 1.0,
            'COTReport': 1.0
        })
    )
