import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SuperTrend_VolumeOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SuperTrend und VolumeOscillator
    """
    
    params = (
        ('indicators', {
            'SuperTrend': {
                'class': SuperTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperTrend'>
            },
            'VolumeOscillator': {
                'class': VolumeOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeOscillator'>
            }
        }),
        ('weights', {
            'SuperTrend': 1.0,
            'VolumeOscillator': 1.0
        })
    )
