import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MurreyMathSignals_VolumeOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MurreyMathSignals und VolumeOscillator
    """
    
    params = (
        ('indicators', {
            'MurreyMathSignals': {
                'class': MurreyMathSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathSignals'>
            },
            'VolumeOscillator': {
                'class': VolumeOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeOscillator'>
            }
        }),
        ('weights', {
            'MurreyMathSignals': 1.0,
            'VolumeOscillator': 1.0
        })
    )
