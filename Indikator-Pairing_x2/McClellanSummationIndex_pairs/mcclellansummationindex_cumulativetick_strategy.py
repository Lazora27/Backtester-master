import backtrader as bt
from ..base_strategy import FlexibleStrategy

class McClellanSummationIndex_CumulativeTick_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von McClellanSummationIndex und CumulativeTick
    """
    
    params = (
        ('indicators', {
            'McClellanSummationIndex': {
                'class': McClellanSummationIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanSummationIndex'>
            },
            'CumulativeTick': {
                'class': CumulativeTick,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CumulativeTick'>
            }
        }),
        ('weights', {
            'McClellanSummationIndex': 1.0,
            'CumulativeTick': 1.0
        })
    )
