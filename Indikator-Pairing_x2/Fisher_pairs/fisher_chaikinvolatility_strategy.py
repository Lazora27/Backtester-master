import backtrader as bt
from ..base_strategy import FlexibleStrategy

class Fisher_ChaikinVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von Fisher und ChaikinVolatility
    """
    
    params = (
        ('indicators', {
            'Fisher': {
                'class': Fisher,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_Fisher'>
            },
            'ChaikinVolatility': {
                'class': ChaikinVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinVolatility'>
            }
        }),
        ('weights', {
            'Fisher': 1.0,
            'ChaikinVolatility': 1.0
        })
    )
