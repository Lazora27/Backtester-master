import backtrader as bt
from ..base_strategy import FlexibleStrategy

class McClellanOscillator_EaseOfMovement_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von McClellanOscillator und EaseOfMovement
    """
    
    params = (
        ('indicators', {
            'McClellanOscillator': {
                'class': McClellanOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanOscillator'>
            },
            'EaseOfMovement': {
                'class': EaseOfMovement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EaseOfMovement1'>
            }
        }),
        ('weights', {
            'McClellanOscillator': 1.0,
            'EaseOfMovement': 1.0
        })
    )
