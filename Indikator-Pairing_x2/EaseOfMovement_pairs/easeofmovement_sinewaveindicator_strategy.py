import backtrader as bt
from ..base_strategy import FlexibleStrategy

class EaseOfMovement_SineWaveIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von EaseOfMovement und SineWaveIndicator
    """
    
    params = (
        ('indicators', {
            'EaseOfMovement': {
                'class': EaseOfMovement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EaseOfMovement1'>
            },
            'SineWaveIndicator': {
                'class': SineWaveIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveIndicator'>
            }
        }),
        ('weights', {
            'EaseOfMovement': 1.0,
            'SineWaveIndicator': 1.0
        })
    )
