import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VortexIndicator_WeightedMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VortexIndicator und WeightedMovingAverage
    """
    
    params = (
        ('indicators', {
            'VortexIndicator': {
                'class': VortexIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VortexIndicator'>
            },
            'WeightedMovingAverage': {
                'class': WeightedMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedMovingAverage'>
            }
        }),
        ('weights', {
            'VortexIndicator': 1.0,
            'WeightedMovingAverage': 1.0
        })
    )
