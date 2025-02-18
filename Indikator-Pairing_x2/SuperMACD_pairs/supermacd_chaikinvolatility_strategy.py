import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SuperMACD_ChaikinVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SuperMACD und ChaikinVolatility
    """
    
    params = (
        ('indicators', {
            'SuperMACD': {
                'class': SuperMACD,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperMACD'>
            },
            'ChaikinVolatility': {
                'class': ChaikinVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinVolatility'>
            }
        }),
        ('weights', {
            'SuperMACD': 1.0,
            'ChaikinVolatility': 1.0
        })
    )
