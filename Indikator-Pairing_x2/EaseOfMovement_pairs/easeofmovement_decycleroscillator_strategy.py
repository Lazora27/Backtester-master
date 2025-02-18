import backtrader as bt
from ..base_strategy import FlexibleStrategy

class EaseOfMovement_DecyclerOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von EaseOfMovement und DecyclerOscillator
    """
    
    params = (
        ('indicators', {
            'EaseOfMovement': {
                'class': EaseOfMovement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EaseOfMovement1'>
            },
            'DecyclerOscillator': {
                'class': DecyclerOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DecyclerOscillator'>
            }
        }),
        ('weights', {
            'EaseOfMovement': 1.0,
            'DecyclerOscillator': 1.0
        })
    )
