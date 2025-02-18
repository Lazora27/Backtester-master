import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VortexIndicator_KlingerVolumeOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VortexIndicator und KlingerVolumeOscillator
    """
    
    params = (
        ('indicators', {
            'VortexIndicator': {
                'class': VortexIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VortexIndicator'>
            },
            'KlingerVolumeOscillator': {
                'class': KlingerVolumeOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KlingerVolumeOscillator'>
            }
        }),
        ('weights', {
            'VortexIndicator': 1.0,
            'KlingerVolumeOscillator': 1.0
        })
    )
