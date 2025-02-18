import backtrader as bt
from ..base_strategy import FlexibleStrategy

class EaseOfMovement_CyberCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von EaseOfMovement und CyberCycle
    """
    
    params = (
        ('indicators', {
            'EaseOfMovement': {
                'class': EaseOfMovement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EaseOfMovement1'>
            },
            'CyberCycle': {
                'class': CyberCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycle'>
            }
        }),
        ('weights', {
            'EaseOfMovement': 1.0,
            'CyberCycle': 1.0
        })
    )
