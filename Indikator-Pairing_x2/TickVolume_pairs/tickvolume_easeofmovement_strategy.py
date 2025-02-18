import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickVolume_EaseOfMovement_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickVolume und EaseOfMovement
    """
    
    params = (
        ('indicators', {
            'TickVolume': {
                'class': TickVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickVolume'>
            },
            'EaseOfMovement': {
                'class': EaseOfMovement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EaseOfMovement1'>
            }
        }),
        ('weights', {
            'TickVolume': 1.0,
            'EaseOfMovement': 1.0
        })
    )
