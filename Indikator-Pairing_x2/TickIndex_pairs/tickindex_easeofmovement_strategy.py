import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickIndex_EaseOfMovement_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickIndex und EaseOfMovement
    """
    
    params = (
        ('indicators', {
            'TickIndex': {
                'class': TickIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickIndex'>
            },
            'EaseOfMovement': {
                'class': EaseOfMovement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EaseOfMovement1'>
            }
        }),
        ('weights', {
            'TickIndex': 1.0,
            'EaseOfMovement': 1.0
        })
    )
