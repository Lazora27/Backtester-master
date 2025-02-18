import backtrader as bt
from ..base_strategy import FlexibleStrategy

class McClellanSummationIndex_ExponentialMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von McClellanSummationIndex und ExponentialMovingAverage
    """
    
    params = (
        ('indicators', {
            'McClellanSummationIndex': {
                'class': McClellanSummationIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanSummationIndex'>
            },
            'ExponentialMovingAverage': {
                'class': ExponentialMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExponentialMovingAverage'>
            }
        }),
        ('weights', {
            'McClellanSummationIndex': 1.0,
            'ExponentialMovingAverage': 1.0
        })
    )
