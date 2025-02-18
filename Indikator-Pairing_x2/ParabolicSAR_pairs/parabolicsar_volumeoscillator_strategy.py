import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ParabolicSAR_VolumeOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ParabolicSAR und VolumeOscillator
    """
    
    params = (
        ('indicators', {
            'ParabolicSAR': {
                'class': ParabolicSAR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicSAR'>
            },
            'VolumeOscillator': {
                'class': VolumeOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeOscillator'>
            }
        }),
        ('weights', {
            'ParabolicSAR': 1.0,
            'VolumeOscillator': 1.0
        })
    )
