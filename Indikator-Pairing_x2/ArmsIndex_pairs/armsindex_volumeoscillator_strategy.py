import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ArmsIndex_VolumeOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ArmsIndex und VolumeOscillator
    """
    
    params = (
        ('indicators', {
            'ArmsIndex': {
                'class': ArmsIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ArmsIndex'>
            },
            'VolumeOscillator': {
                'class': VolumeOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeOscillator'>
            }
        }),
        ('weights', {
            'ArmsIndex': 1.0,
            'VolumeOscillator': 1.0
        })
    )
