import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RelativeMomentumIndex_WeightedMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RelativeMomentumIndex und WeightedMovingAverage
    """
    
    params = (
        ('indicators', {
            'RelativeMomentumIndex': {
                'class': RelativeMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeMomentumIndex'>
            },
            'WeightedMovingAverage': {
                'class': WeightedMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedMovingAverage'>
            }
        }),
        ('weights', {
            'RelativeMomentumIndex': 1.0,
            'WeightedMovingAverage': 1.0
        })
    )
