import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CoppockCurve_WeightedMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CoppockCurve und WeightedMovingAverage
    """
    
    params = (
        ('indicators', {
            'CoppockCurve': {
                'class': CoppockCurve,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CoppockCurve'>
            },
            'WeightedMovingAverage': {
                'class': WeightedMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedMovingAverage'>
            }
        }),
        ('weights', {
            'CoppockCurve': 1.0,
            'WeightedMovingAverage': 1.0
        })
    )
