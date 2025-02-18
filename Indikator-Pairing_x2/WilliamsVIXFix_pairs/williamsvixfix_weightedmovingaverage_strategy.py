import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsVIXFix_WeightedMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsVIXFix und WeightedMovingAverage
    """
    
    params = (
        ('indicators', {
            'WilliamsVIXFix': {
                'class': WilliamsVIXFix,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsVIXFix'>
            },
            'WeightedMovingAverage': {
                'class': WeightedMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedMovingAverage'>
            }
        }),
        ('weights', {
            'WilliamsVIXFix': 1.0,
            'WeightedMovingAverage': 1.0
        })
    )
