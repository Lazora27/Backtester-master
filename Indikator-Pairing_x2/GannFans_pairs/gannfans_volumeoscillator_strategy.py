import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannFans_VolumeOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannFans und VolumeOscillator
    """
    
    params = (
        ('indicators', {
            'GannFans': {
                'class': GannFans,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannFans'>
            },
            'VolumeOscillator': {
                'class': VolumeOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeOscillator'>
            }
        }),
        ('weights', {
            'GannFans': 1.0,
            'VolumeOscillator': 1.0
        })
    )
