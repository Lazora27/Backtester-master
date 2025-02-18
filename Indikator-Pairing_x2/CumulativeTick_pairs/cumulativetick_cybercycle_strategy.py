import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CumulativeTick_CyberCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CumulativeTick und CyberCycle
    """
    
    params = (
        ('indicators', {
            'CumulativeTick': {
                'class': CumulativeTick,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CumulativeTick'>
            },
            'CyberCycle': {
                'class': CyberCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycle'>
            }
        }),
        ('weights', {
            'CumulativeTick': 1.0,
            'CyberCycle': 1.0
        })
    )
