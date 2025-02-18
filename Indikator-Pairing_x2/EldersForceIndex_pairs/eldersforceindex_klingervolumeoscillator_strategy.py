import backtrader as bt
from ..base_strategy import FlexibleStrategy

class EldersForceIndex_KlingerVolumeOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von EldersForceIndex und KlingerVolumeOscillator
    """
    
    params = (
        ('indicators', {
            'EldersForceIndex': {
                'class': EldersForceIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EldersForceIndex'>
            },
            'KlingerVolumeOscillator': {
                'class': KlingerVolumeOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KlingerVolumeOscillator'>
            }
        }),
        ('weights', {
            'EldersForceIndex': 1.0,
            'KlingerVolumeOscillator': 1.0
        })
    )
