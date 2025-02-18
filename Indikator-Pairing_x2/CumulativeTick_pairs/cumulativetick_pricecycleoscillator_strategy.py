import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CumulativeTick_PriceCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CumulativeTick und PriceCycleOscillator
    """
    
    params = (
        ('indicators', {
            'CumulativeTick': {
                'class': CumulativeTick,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CumulativeTick'>
            },
            'PriceCycleOscillator': {
                'class': PriceCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceCycleOscillator'>
            }
        }),
        ('weights', {
            'CumulativeTick': 1.0,
            'PriceCycleOscillator': 1.0
        })
    )
