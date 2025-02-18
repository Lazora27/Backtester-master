import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DynamicMomentumIndex_WeightedMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DynamicMomentumIndex und WeightedMovingAverage
    """
    
    params = (
        ('indicators', {
            'DynamicMomentumIndex': {
                'class': DynamicMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DynamicMomentumIndex'>
            },
            'WeightedMovingAverage': {
                'class': WeightedMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedMovingAverage'>
            }
        }),
        ('weights', {
            'DynamicMomentumIndex': 1.0,
            'WeightedMovingAverage': 1.0
        })
    )
