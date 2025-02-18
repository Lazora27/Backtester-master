import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FearGreedIndex_VolumeOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FearGreedIndex und VolumeOscillator
    """
    
    params = (
        ('indicators', {
            'FearGreedIndex': {
                'class': FearGreedIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FearGreedIndex'>
            },
            'VolumeOscillator': {
                'class': VolumeOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeOscillator'>
            }
        }),
        ('weights', {
            'FearGreedIndex': 1.0,
            'VolumeOscillator': 1.0
        })
    )
