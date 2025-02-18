import backtrader as bt
from ..base_strategy import FlexibleStrategy

class COTReport_MarketCycleIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von COTReport und MarketCycleIndicator
    """
    
    params = (
        ('indicators', {
            'COTReport': {
                'class': COTReport,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_COTReport'>
            },
            'MarketCycleIndicator': {
                'class': MarketCycleIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketCycleIndicator'>
            }
        }),
        ('weights', {
            'COTReport': 1.0,
            'MarketCycleIndicator': 1.0
        })
    )
