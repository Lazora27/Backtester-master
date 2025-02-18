import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeOscillator_WeightedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeOscillator und WeightedCycle
    """
    
    params = (
        ('indicators', {
            'VolumeOscillator': {
                'class': VolumeOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeOscillator'>
            },
            'WeightedCycle': {
                'class': WeightedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedCycle'>
            }
        }),
        ('weights', {
            'VolumeOscillator': 1.0,
            'WeightedCycle': 1.0
        })
    )
