import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickActivityIndex_EaseOfMovement_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickActivityIndex und EaseOfMovement
    """
    
    params = (
        ('indicators', {
            'TickActivityIndex': {
                'class': TickActivityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickActivityIndex'>
            },
            'EaseOfMovement': {
                'class': EaseOfMovement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EaseOfMovement1'>
            }
        }),
        ('weights', {
            'TickActivityIndex': 1.0,
            'EaseOfMovement': 1.0
        })
    )
