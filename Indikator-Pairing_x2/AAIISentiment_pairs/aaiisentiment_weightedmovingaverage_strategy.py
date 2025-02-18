import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AAIISentiment_WeightedMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AAIISentiment und WeightedMovingAverage
    """
    
    params = (
        ('indicators', {
            'AAIISentiment': {
                'class': AAIISentiment,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AAIISentiment'>
            },
            'WeightedMovingAverage': {
                'class': WeightedMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedMovingAverage'>
            }
        }),
        ('weights', {
            'AAIISentiment': 1.0,
            'WeightedMovingAverage': 1.0
        })
    )
