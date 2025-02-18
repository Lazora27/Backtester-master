import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ExponentialMovingAverage_MassIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ExponentialMovingAverage und MassIndex
    """
    
    params = (
        ('indicators', {
            'ExponentialMovingAverage': {
                'class': ExponentialMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExponentialMovingAverage'>
            },
            'MassIndex': {
                'class': MassIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MassIndex'>
            }
        }),
        ('weights', {
            'ExponentialMovingAverage': 1.0,
            'MassIndex': 1.0
        })
    )
