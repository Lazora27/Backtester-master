import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CumulativeTick_CoppockCurve_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CumulativeTick und CoppockCurve
    """
    
    params = (
        ('indicators', {
            'CumulativeTick': {
                'class': CumulativeTick,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CumulativeTick'>
            },
            'CoppockCurve': {
                'class': CoppockCurve,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CoppockCurve'>
            }
        }),
        ('weights', {
            'CumulativeTick': 1.0,
            'CoppockCurve': 1.0
        })
    )
