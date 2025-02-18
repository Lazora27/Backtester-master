import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CumulativeTick_MomentumTrendStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CumulativeTick und MomentumTrendStrength
    """
    
    params = (
        ('indicators', {
            'CumulativeTick': {
                'class': CumulativeTick,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CumulativeTick'>
            },
            'MomentumTrendStrength': {
                'class': MomentumTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumTrendStrength'>
            }
        }),
        ('weights', {
            'CumulativeTick': 1.0,
            'MomentumTrendStrength': 1.0
        })
    )
