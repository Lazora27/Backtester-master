import backtrader as bt
from ..base_strategy import FlexibleStrategy

class EaseOfMovement_CCITurbo_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von EaseOfMovement und CCITurbo
    """
    
    params = (
        ('indicators', {
            'EaseOfMovement': {
                'class': EaseOfMovement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EaseOfMovement1'>
            },
            'CCITurbo': {
                'class': CCITurbo,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CCITurbo'>
            }
        }),
        ('weights', {
            'EaseOfMovement': 1.0,
            'CCITurbo': 1.0
        })
    )
