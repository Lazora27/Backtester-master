import backtrader as bt
from ..base_strategy import FlexibleStrategy

class KlingerVolumeOscillator_EhlersDecycler_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von KlingerVolumeOscillator und EhlersDecycler
    """
    
    params = (
        ('indicators', {
            'KlingerVolumeOscillator': {
                'class': KlingerVolumeOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KlingerVolumeOscillator'>
            },
            'EhlersDecycler': {
                'class': EhlersDecycler,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersDecycler'>
            }
        }),
        ('weights', {
            'KlingerVolumeOscillator': 1.0,
            'EhlersDecycler': 1.0
        })
    )
