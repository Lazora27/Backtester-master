import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CumulativeTick_WolfeWaveIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CumulativeTick und WolfeWaveIndicator
    """
    
    params = (
        ('indicators', {
            'CumulativeTick': {
                'class': CumulativeTick,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CumulativeTick'>
            },
            'WolfeWaveIndicator': {
                'class': WolfeWaveIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaveIndicator'>
            }
        }),
        ('weights', {
            'CumulativeTick': 1.0,
            'WolfeWaveIndicator': 1.0
        })
    )
