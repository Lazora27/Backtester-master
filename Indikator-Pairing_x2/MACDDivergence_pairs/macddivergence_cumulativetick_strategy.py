import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDDivergence_CumulativeTick_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDDivergence und CumulativeTick
    """
    
    params = (
        ('indicators', {
            'MACDDivergence': {
                'class': MACDDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDDivergence'>
            },
            'CumulativeTick': {
                'class': CumulativeTick,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CumulativeTick'>
            }
        }),
        ('weights', {
            'MACDDivergence': 1.0,
            'CumulativeTick': 1.0
        })
    )
