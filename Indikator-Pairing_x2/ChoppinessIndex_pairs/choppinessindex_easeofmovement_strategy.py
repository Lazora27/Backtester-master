import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChoppinessIndex_EaseOfMovement_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChoppinessIndex und EaseOfMovement
    """
    
    params = (
        ('indicators', {
            'ChoppinessIndex': {
                'class': ChoppinessIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChoppinessIndex'>
            },
            'EaseOfMovement': {
                'class': EaseOfMovement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EaseOfMovement1'>
            }
        }),
        ('weights', {
            'ChoppinessIndex': 1.0,
            'EaseOfMovement': 1.0
        })
    )
