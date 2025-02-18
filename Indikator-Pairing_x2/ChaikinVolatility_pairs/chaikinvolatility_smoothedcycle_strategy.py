import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChaikinVolatility_SmoothedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChaikinVolatility und SmoothedCycle
    """
    
    params = (
        ('indicators', {
            'ChaikinVolatility': {
                'class': ChaikinVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinVolatility'>
            },
            'SmoothedCycle': {
                'class': SmoothedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedCycle'>
            }
        }),
        ('weights', {
            'ChaikinVolatility': 1.0,
            'SmoothedCycle': 1.0
        })
    )
