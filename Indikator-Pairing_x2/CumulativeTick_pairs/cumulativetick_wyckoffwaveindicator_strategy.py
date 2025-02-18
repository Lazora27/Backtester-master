import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CumulativeTick_WyckoffWaveIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CumulativeTick und WyckoffWaveIndicator
    """
    
    params = (
        ('indicators', {
            'CumulativeTick': {
                'class': CumulativeTick,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CumulativeTick'>
            },
            'WyckoffWaveIndicator': {
                'class': WyckoffWaveIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WyckoffWaveIndicator'>
            }
        }),
        ('weights', {
            'CumulativeTick': 1.0,
            'WyckoffWaveIndicator': 1.0
        })
    )
