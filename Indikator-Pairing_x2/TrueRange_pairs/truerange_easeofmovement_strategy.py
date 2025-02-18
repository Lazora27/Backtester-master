import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrueRange_EaseOfMovement_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrueRange und EaseOfMovement
    """
    
    params = (
        ('indicators', {
            'TrueRange': {
                'class': TrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRange1'>
            },
            'EaseOfMovement': {
                'class': EaseOfMovement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EaseOfMovement1'>
            }
        }),
        ('weights', {
            'TrueRange': 1.0,
            'EaseOfMovement': 1.0
        })
    )
