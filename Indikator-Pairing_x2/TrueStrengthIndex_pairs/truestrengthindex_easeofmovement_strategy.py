import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrueStrengthIndex_EaseOfMovement_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrueStrengthIndex und EaseOfMovement
    """
    
    params = (
        ('indicators', {
            'TrueStrengthIndex': {
                'class': TrueStrengthIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueStrengthIndex'>
            },
            'EaseOfMovement': {
                'class': EaseOfMovement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EaseOfMovement1'>
            }
        }),
        ('weights', {
            'TrueStrengthIndex': 1.0,
            'EaseOfMovement': 1.0
        })
    )
