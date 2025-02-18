import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AverageTrueRange_VolumeOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AverageTrueRange und VolumeOscillator
    """
    
    params = (
        ('indicators', {
            'AverageTrueRange': {
                'class': AverageTrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageTrueRange1'>
            },
            'VolumeOscillator': {
                'class': VolumeOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeOscillator'>
            }
        }),
        ('weights', {
            'AverageTrueRange': 1.0,
            'VolumeOscillator': 1.0
        })
    )
