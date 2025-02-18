import backtrader as bt
from ..base_strategy import FlexibleStrategy

class EaseOfMovement_CyberCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von EaseOfMovement und CyberCycleOscillator
    """
    
    params = (
        ('indicators', {
            'EaseOfMovement': {
                'class': EaseOfMovement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EaseOfMovement1'>
            },
            'CyberCycleOscillator': {
                'class': CyberCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycleOscillator'>
            }
        }),
        ('weights', {
            'EaseOfMovement': 1.0,
            'CyberCycleOscillator': 1.0
        })
    )
