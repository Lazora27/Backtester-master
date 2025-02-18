import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PercentageVolumeOscillator_TrueStrengthIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PercentageVolumeOscillator und TrueStrengthIndex
    """
    
    params = (
        ('indicators', {
            'PercentageVolumeOscillator': {
                'class': PercentageVolumeOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PercentageVolumeOscillator'>
            },
            'TrueStrengthIndex': {
                'class': TrueStrengthIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueStrengthIndex'>
            }
        }),
        ('weights', {
            'PercentageVolumeOscillator': 1.0,
            'TrueStrengthIndex': 1.0
        })
    )
