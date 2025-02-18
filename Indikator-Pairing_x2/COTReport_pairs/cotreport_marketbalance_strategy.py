import backtrader as bt
from ..base_strategy import FlexibleStrategy

class COTReport_MarketBalance_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von COTReport und MarketBalance
    """
    
    params = (
        ('indicators', {
            'COTReport': {
                'class': COTReport,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_COTReport'>
            },
            'MarketBalance': {
                'class': MarketBalance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketBalance'>
            }
        }),
        ('weights', {
            'COTReport': 1.0,
            'MarketBalance': 1.0
        })
    )
