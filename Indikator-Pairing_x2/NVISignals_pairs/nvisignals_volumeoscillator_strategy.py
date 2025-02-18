import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NVISignals_VolumeOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NVISignals und VolumeOscillator
    """
    
    params = (
        ('indicators', {
            'NVISignals': {
                'class': NVISignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NVISignals'>
            },
            'VolumeOscillator': {
                'class': VolumeOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeOscillator'>
            }
        }),
        ('weights', {
            'NVISignals': 1.0,
            'VolumeOscillator': 1.0
        })
    )
