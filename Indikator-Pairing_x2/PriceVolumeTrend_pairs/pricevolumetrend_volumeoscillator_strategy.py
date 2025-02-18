import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceVolumeTrend_VolumeOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceVolumeTrend und VolumeOscillator
    """
    
    params = (
        ('indicators', {
            'PriceVolumeTrend': {
                'class': PriceVolumeTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceVolumeTrend'>
            },
            'VolumeOscillator': {
                'class': VolumeOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeOscillator'>
            }
        }),
        ('weights', {
            'PriceVolumeTrend': 1.0,
            'VolumeOscillator': 1.0
        })
    )
