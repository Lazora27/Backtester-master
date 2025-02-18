import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsR_ChaikinVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsR und ChaikinVolatility
    """
    
    params = (
        ('indicators', {
            'WilliamsR': {
                'class': WilliamsR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsR1'>
            },
            'ChaikinVolatility': {
                'class': ChaikinVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinVolatility'>
            }
        }),
        ('weights', {
            'WilliamsR': 1.0,
            'ChaikinVolatility': 1.0
        })
    )
