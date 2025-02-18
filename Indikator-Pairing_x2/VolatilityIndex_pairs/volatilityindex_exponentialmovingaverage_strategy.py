import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolatilityIndex_ExponentialMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolatilityIndex und ExponentialMovingAverage
    """
    
    params = (
        ('indicators', {
            'VolatilityIndex': {
                'class': VolatilityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolatilityIndex'>
            },
            'ExponentialMovingAverage': {
                'class': ExponentialMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExponentialMovingAverage'>
            }
        }),
        ('weights', {
            'VolatilityIndex': 1.0,
            'ExponentialMovingAverage': 1.0
        })
    )
