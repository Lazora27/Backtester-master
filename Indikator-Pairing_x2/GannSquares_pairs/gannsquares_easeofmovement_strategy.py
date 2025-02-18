import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannSquares_EaseOfMovement_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannSquares und EaseOfMovement
    """
    
    params = (
        ('indicators', {
            'GannSquares': {
                'class': GannSquares,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquares'>
            },
            'EaseOfMovement': {
                'class': EaseOfMovement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EaseOfMovement1'>
            }
        }),
        ('weights', {
            'GannSquares': 1.0,
            'EaseOfMovement': 1.0
        })
    )
