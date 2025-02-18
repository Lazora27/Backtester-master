import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HullMovingAverage_ChaikinVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HullMovingAverage und ChaikinVolatility
    """
    
    params = (
        ('indicators', {
            'HullMovingAverage': {
                'class': HullMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HullMovingAverage'>
            },
            'ChaikinVolatility': {
                'class': ChaikinVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinVolatility'>
            }
        }),
        ('weights', {
            'HullMovingAverage': 1.0,
            'ChaikinVolatility': 1.0
        })
    )
