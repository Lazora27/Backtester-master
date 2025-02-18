import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AwesomeOscillator_EaseOfMovement_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AwesomeOscillator und EaseOfMovement
    """
    
    params = (
        ('indicators', {
            'AwesomeOscillator': {
                'class': AwesomeOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AwesomeOscillator1'>
            },
            'EaseOfMovement': {
                'class': EaseOfMovement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EaseOfMovement1'>
            }
        }),
        ('weights', {
            'AwesomeOscillator': 1.0,
            'EaseOfMovement': 1.0
        })
    )
