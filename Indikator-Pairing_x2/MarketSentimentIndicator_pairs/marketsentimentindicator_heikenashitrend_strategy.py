import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketSentimentIndicator_HeikenAshiTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketSentimentIndicator und HeikenAshiTrend
    """
    
    params = (
        ('indicators', {
            'MarketSentimentIndicator': {
                'class': MarketSentimentIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketSentimentIndicator'>
            },
            'HeikenAshiTrend': {
                'class': HeikenAshiTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HeikenAshiTrend'>
            }
        }),
        ('weights', {
            'MarketSentimentIndicator': 1.0,
            'HeikenAshiTrend': 1.0
        })
    )
