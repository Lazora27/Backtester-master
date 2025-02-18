import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannSquareReversal_EaseOfMovement_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannSquareReversal und EaseOfMovement
    """
    
    params = (
        ('indicators', {
            'GannSquareReversal': {
                'class': GannSquareReversal,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquareReversal'>
            },
            'EaseOfMovement': {
                'class': EaseOfMovement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EaseOfMovement1'>
            }
        }),
        ('weights', {
            'GannSquareReversal': 1.0,
            'EaseOfMovement': 1.0
        })
    )
