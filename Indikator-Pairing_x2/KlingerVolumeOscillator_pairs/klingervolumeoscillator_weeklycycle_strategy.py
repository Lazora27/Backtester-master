import backtrader as bt
from ..base_strategy import FlexibleStrategy

class KlingerVolumeOscillator_WeeklyCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von KlingerVolumeOscillator und WeeklyCycle
    """
    
    params = (
        ('indicators', {
            'KlingerVolumeOscillator': {
                'class': KlingerVolumeOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KlingerVolumeOscillator'>
            },
            'WeeklyCycle': {
                'class': WeeklyCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeeklyCycle'>
            }
        }),
        ('weights', {
            'KlingerVolumeOscillator': 1.0,
            'WeeklyCycle': 1.0
        })
    )
