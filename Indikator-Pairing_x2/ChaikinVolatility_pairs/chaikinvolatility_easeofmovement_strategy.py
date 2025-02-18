import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChaikinVolatility_EaseOfMovement_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChaikinVolatility und EaseOfMovement
    """
    
    params = (
        ('indicators', {
            'ChaikinVolatility': {
                'class': ChaikinVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinVolatility'>
            },
            'EaseOfMovement': {
                'class': EaseOfMovement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EaseOfMovement1'>
            }
        }),
        ('weights', {
            'ChaikinVolatility': 1.0,
            'EaseOfMovement': 1.0
        })
    )
