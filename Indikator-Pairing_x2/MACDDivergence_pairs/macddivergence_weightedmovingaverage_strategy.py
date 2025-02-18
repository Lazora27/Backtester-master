import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDDivergence_WeightedMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDDivergence und WeightedMovingAverage
    """
    
    params = (
        ('indicators', {
            'MACDDivergence': {
                'class': MACDDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDDivergence'>
            },
            'WeightedMovingAverage': {
                'class': WeightedMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedMovingAverage'>
            }
        }),
        ('weights', {
            'MACDDivergence': 1.0,
            'WeightedMovingAverage': 1.0
        })
    )
