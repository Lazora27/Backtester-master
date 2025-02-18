import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BarStrength_EaseOfMovement_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BarStrength und EaseOfMovement
    """
    
    params = (
        ('indicators', {
            'BarStrength': {
                'class': BarStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BarStrength'>
            },
            'EaseOfMovement': {
                'class': EaseOfMovement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EaseOfMovement1'>
            }
        }),
        ('weights', {
            'BarStrength': 1.0,
            'EaseOfMovement': 1.0
        })
    )
