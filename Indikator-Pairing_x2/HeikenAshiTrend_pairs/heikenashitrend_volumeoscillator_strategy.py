import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HeikenAshiTrend_VolumeOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HeikenAshiTrend und VolumeOscillator
    """
    
    params = (
        ('indicators', {
            'HeikenAshiTrend': {
                'class': HeikenAshiTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HeikenAshiTrend'>
            },
            'VolumeOscillator': {
                'class': VolumeOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeOscillator'>
            }
        }),
        ('weights', {
            'HeikenAshiTrend': 1.0,
            'VolumeOscillator': 1.0
        })
    )
