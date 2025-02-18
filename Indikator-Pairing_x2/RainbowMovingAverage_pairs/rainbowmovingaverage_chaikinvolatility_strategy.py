import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RainbowMovingAverage_ChaikinVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RainbowMovingAverage und ChaikinVolatility
    """
    
    params = (
        ('indicators', {
            'RainbowMovingAverage': {
                'class': RainbowMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RainbowMovingAverage'>
            },
            'ChaikinVolatility': {
                'class': ChaikinVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinVolatility'>
            }
        }),
        ('weights', {
            'RainbowMovingAverage': 1.0,
            'ChaikinVolatility': 1.0
        })
    )
