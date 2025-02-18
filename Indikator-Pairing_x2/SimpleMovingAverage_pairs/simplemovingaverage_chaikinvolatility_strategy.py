import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SimpleMovingAverage_ChaikinVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SimpleMovingAverage und ChaikinVolatility
    """
    
    params = (
        ('indicators', {
            'SimpleMovingAverage': {
                'class': SimpleMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SimpleMovingAverage'>
            },
            'ChaikinVolatility': {
                'class': ChaikinVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinVolatility'>
            }
        }),
        ('weights', {
            'SimpleMovingAverage': 1.0,
            'ChaikinVolatility': 1.0
        })
    )
