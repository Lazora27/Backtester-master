import backtrader as bt
from ..base_strategy import FlexibleStrategy

class EldersForceIndex_CumulativeTick_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von EldersForceIndex und CumulativeTick
    """
    
    params = (
        ('indicators', {
            'EldersForceIndex': {
                'class': EldersForceIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EldersForceIndex'>
            },
            'CumulativeTick': {
                'class': CumulativeTick,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CumulativeTick'>
            }
        }),
        ('weights', {
            'EldersForceIndex': 1.0,
            'CumulativeTick': 1.0
        })
    )
