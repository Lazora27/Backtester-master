import backtrader as bt
from ..base_strategy import FlexibleStrategy

class COTReport_MarketSentimentIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von COTReport und MarketSentimentIndicator
    """
    
    params = (
        ('indicators', {
            'COTReport': {
                'class': COTReport,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_COTReport'>
            },
            'MarketSentimentIndicator': {
                'class': MarketSentimentIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketSentimentIndicator'>
            }
        }),
        ('weights', {
            'COTReport': 1.0,
            'MarketSentimentIndicator': 1.0
        })
    )
