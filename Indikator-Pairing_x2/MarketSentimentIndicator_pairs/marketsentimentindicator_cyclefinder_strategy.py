import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketSentimentIndicator_CycleFinder_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketSentimentIndicator und CycleFinder
    """
    
    params = (
        ('indicators', {
            'MarketSentimentIndicator': {
                'class': MarketSentimentIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketSentimentIndicator'>
            },
            'CycleFinder': {
                'class': CycleFinder,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CycleFinder'>
            }
        }),
        ('weights', {
            'MarketSentimentIndicator': 1.0,
            'CycleFinder': 1.0
        })
    )
