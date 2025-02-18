import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BarStrength_VolumeOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BarStrength und VolumeOscillator
    """
    
    params = (
        ('indicators', {
            'BarStrength': {
                'class': BarStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BarStrength'>
            },
            'VolumeOscillator': {
                'class': VolumeOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeOscillator'>
            }
        }),
        ('weights', {
            'BarStrength': 1.0,
            'VolumeOscillator': 1.0
        })
    )
