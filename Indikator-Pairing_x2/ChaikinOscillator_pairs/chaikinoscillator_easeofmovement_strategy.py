import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChaikinOscillator_EaseOfMovement_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChaikinOscillator und EaseOfMovement
    """
    
    params = (
        ('indicators', {
            'ChaikinOscillator': {
                'class': ChaikinOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinOscillator'>
            },
            'EaseOfMovement': {
                'class': EaseOfMovement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EaseOfMovement1'>
            }
        }),
        ('weights', {
            'ChaikinOscillator': 1.0,
            'EaseOfMovement': 1.0
        })
    )
