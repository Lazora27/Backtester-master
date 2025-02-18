import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketSentimentIndicator_SharpeRatioIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketSentimentIndicator und SharpeRatioIndicator
    """
    
    params = (
        ('indicators', {
            'MarketSentimentIndicator': {
                'class': MarketSentimentIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketSentimentIndicator'>
            },
            'SharpeRatioIndicator': {
                'class': SharpeRatioIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SharpeRatioIndicator'>
            }
        }),
        ('weights', {
            'MarketSentimentIndicator': 1.0,
            'SharpeRatioIndicator': 1.0
        })
    )
