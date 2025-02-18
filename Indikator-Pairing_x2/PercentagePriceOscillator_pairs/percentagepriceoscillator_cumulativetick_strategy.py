import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PercentagePriceOscillator_CumulativeTick_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PercentagePriceOscillator und CumulativeTick
    """
    
    params = (
        ('indicators', {
            'PercentagePriceOscillator': {
                'class': PercentagePriceOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PercentagePriceOscillator'>
            },
            'CumulativeTick': {
                'class': CumulativeTick,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CumulativeTick'>
            }
        }),
        ('weights', {
            'PercentagePriceOscillator': 1.0,
            'CumulativeTick': 1.0
        })
    )
