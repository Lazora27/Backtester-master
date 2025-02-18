import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ExponentialMovingAverage_UlcerIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ExponentialMovingAverage und UlcerIndex
    """
    
    params = (
        ('indicators', {
            'ExponentialMovingAverage': {
                'class': ExponentialMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExponentialMovingAverage'>
            },
            'UlcerIndex': {
                'class': UlcerIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndex'>
            }
        }),
        ('weights', {
            'ExponentialMovingAverage': 1.0,
            'UlcerIndex': 1.0
        })
    )
