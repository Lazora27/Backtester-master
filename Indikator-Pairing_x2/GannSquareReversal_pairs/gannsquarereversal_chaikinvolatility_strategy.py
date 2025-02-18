import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannSquareReversal_ChaikinVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannSquareReversal und ChaikinVolatility
    """
    
    params = (
        ('indicators', {
            'GannSquareReversal': {
                'class': GannSquareReversal,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquareReversal'>
            },
            'ChaikinVolatility': {
                'class': ChaikinVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinVolatility'>
            }
        }),
        ('weights', {
            'GannSquareReversal': 1.0,
            'ChaikinVolatility': 1.0
        })
    )
