import backtrader as bt
from ..base_strategy import FlexibleStrategy

class UlcerIndex_VolumeOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von UlcerIndex und VolumeOscillator
    """
    
    params = (
        ('indicators', {
            'UlcerIndex': {
                'class': UlcerIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndex'>
            },
            'VolumeOscillator': {
                'class': VolumeOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeOscillator'>
            }
        }),
        ('weights', {
            'UlcerIndex': 1.0,
            'VolumeOscillator': 1.0
        })
    )
