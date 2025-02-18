import backtrader as bt
from ..base_strategy import FlexibleStrategy

class EaseOfMovement_PhaseDivergence_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von EaseOfMovement und PhaseDivergence
    """
    
    params = (
        ('indicators', {
            'EaseOfMovement': {
                'class': EaseOfMovement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EaseOfMovement1'>
            },
            'PhaseDivergence': {
                'class': PhaseDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PhaseDivergence'>
            }
        }),
        ('weights', {
            'EaseOfMovement': 1.0,
            'PhaseDivergence': 1.0
        })
    )
