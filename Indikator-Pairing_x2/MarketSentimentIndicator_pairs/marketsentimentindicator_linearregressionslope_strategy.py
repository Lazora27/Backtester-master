import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketSentimentIndicator_LinearRegressionSlope_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketSentimentIndicator und LinearRegressionSlope
    """
    
    params = (
        ('indicators', {
            'MarketSentimentIndicator': {
                'class': MarketSentimentIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketSentimentIndicator'>
            },
            'LinearRegressionSlope': {
                'class': LinearRegressionSlope,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionSlope'>
            }
        }),
        ('weights', {
            'MarketSentimentIndicator': 1.0,
            'LinearRegressionSlope': 1.0
        })
    )
