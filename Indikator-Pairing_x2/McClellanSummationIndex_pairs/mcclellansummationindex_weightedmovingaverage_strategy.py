import backtrader as bt
from ..base_strategy import FlexibleStrategy

class McClellanSummationIndex_WeightedMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von McClellanSummationIndex und WeightedMovingAverage
    """
    
    params = (
        ('indicators', {
            'McClellanSummationIndex': {
                'class': McClellanSummationIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanSummationIndex'>
            },
            'WeightedMovingAverage': {
                'class': WeightedMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedMovingAverage'>
            }
        }),
        ('weights', {
            'McClellanSummationIndex': 1.0,
            'WeightedMovingAverage': 1.0
        })
    )
