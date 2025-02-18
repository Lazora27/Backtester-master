import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RSIDivergence_VolumeOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RSIDivergence und VolumeOscillator
    """
    
    params = (
        ('indicators', {
            'RSIDivergence': {
                'class': RSIDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RSIDivergence'>
            },
            'VolumeOscillator': {
                'class': VolumeOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeOscillator'>
            }
        }),
        ('weights', {
            'RSIDivergence': 1.0,
            'VolumeOscillator': 1.0
        })
    )
