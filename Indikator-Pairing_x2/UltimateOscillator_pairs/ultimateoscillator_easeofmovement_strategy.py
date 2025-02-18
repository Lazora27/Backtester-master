import backtrader as bt
from ..base_strategy import FlexibleStrategy

class UltimateOscillator_EaseOfMovement_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von UltimateOscillator und EaseOfMovement
    """
    
    params = (
        ('indicators', {
            'UltimateOscillator': {
                'class': UltimateOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UltimateOscillator1'>
            },
            'EaseOfMovement': {
                'class': EaseOfMovement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EaseOfMovement1'>
            }
        }),
        ('weights', {
            'UltimateOscillator': 1.0,
            'EaseOfMovement': 1.0
        })
    )
