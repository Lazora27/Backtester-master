import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketSentimentIndicator_TrendCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketSentimentIndicator und TrendCycles
    """
    
    params = (
        ('indicators', {
            'MarketSentimentIndicator': {
                'class': MarketSentimentIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketSentimentIndicator'>
            },
            'TrendCycles': {
                'class': TrendCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendCycles'>
            }
        }),
        ('weights', {
            'MarketSentimentIndicator': 1.0,
            'TrendCycles': 1.0
        })
    )
