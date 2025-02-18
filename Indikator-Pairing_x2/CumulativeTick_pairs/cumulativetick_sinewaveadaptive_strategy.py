import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CumulativeTick_SineWaveAdaptive_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CumulativeTick und SineWaveAdaptive
    """
    
    params = (
        ('indicators', {
            'CumulativeTick': {
                'class': CumulativeTick,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CumulativeTick'>
            },
            'SineWaveAdaptive': {
                'class': SineWaveAdaptive,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveAdaptive'>
            }
        }),
        ('weights', {
            'CumulativeTick': 1.0,
            'SineWaveAdaptive': 1.0
        })
    )
