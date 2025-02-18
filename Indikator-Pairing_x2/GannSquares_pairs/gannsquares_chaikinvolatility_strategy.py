import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannSquares_ChaikinVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannSquares und ChaikinVolatility
    """
    
    params = (
        ('indicators', {
            'GannSquares': {
                'class': GannSquares,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquares'>
            },
            'ChaikinVolatility': {
                'class': ChaikinVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinVolatility'>
            }
        }),
        ('weights', {
            'GannSquares': 1.0,
            'ChaikinVolatility': 1.0
        })
    )
