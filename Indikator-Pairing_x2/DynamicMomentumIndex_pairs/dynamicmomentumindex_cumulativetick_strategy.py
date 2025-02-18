import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DynamicMomentumIndex_CumulativeTick_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DynamicMomentumIndex und CumulativeTick
    """
    
    params = (
        ('indicators', {
            'DynamicMomentumIndex': {
                'class': DynamicMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DynamicMomentumIndex'>
            },
            'CumulativeTick': {
                'class': CumulativeTick,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CumulativeTick'>
            }
        }),
        ('weights', {
            'DynamicMomentumIndex': 1.0,
            'CumulativeTick': 1.0
        })
    )
