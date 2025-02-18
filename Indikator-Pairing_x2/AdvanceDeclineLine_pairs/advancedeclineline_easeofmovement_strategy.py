import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdvanceDeclineLine_EaseOfMovement_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdvanceDeclineLine und EaseOfMovement
    """
    
    params = (
        ('indicators', {
            'AdvanceDeclineLine': {
                'class': AdvanceDeclineLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdvanceDeclineLine'>
            },
            'EaseOfMovement': {
                'class': EaseOfMovement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EaseOfMovement1'>
            }
        }),
        ('weights', {
            'AdvanceDeclineLine': 1.0,
            'EaseOfMovement': 1.0
        })
    )
