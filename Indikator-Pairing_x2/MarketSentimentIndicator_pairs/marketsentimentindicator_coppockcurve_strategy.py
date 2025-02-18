import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketSentimentIndicator_CoppockCurve_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketSentimentIndicator und CoppockCurve
    """
    
    params = (
        ('indicators', {
            'MarketSentimentIndicator': {
                'class': MarketSentimentIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketSentimentIndicator'>
            },
            'CoppockCurve': {
                'class': CoppockCurve,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CoppockCurve'>
            }
        }),
        ('weights', {
            'MarketSentimentIndicator': 1.0,
            'CoppockCurve': 1.0
        })
    )
