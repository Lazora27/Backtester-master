import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PivotPoints_MarketSentimentIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PivotPoints und MarketSentimentIndicator
    """
    
    params = (
        ('indicators', {
            'PivotPoints': {
                'class': PivotPoints,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PivotPoints'>
            },
            'MarketSentimentIndicator': {
                'class': MarketSentimentIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketSentimentIndicator'>
            }
        }),
        ('weights', {
            'PivotPoints': 1.0,
            'MarketSentimentIndicator': 1.0
        })
    )
