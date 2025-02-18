import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrendExhaustion_VolumeOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrendExhaustion und VolumeOscillator
    """
    
    params = (
        ('indicators', {
            'TrendExhaustion': {
                'class': TrendExhaustion,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendExhaustion'>
            },
            'VolumeOscillator': {
                'class': VolumeOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeOscillator'>
            }
        }),
        ('weights', {
            'TrendExhaustion': 1.0,
            'VolumeOscillator': 1.0
        })
    )
