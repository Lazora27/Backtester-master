import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CumulativeTick_CCITurbo_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CumulativeTick und CCITurbo
    """
    
    params = (
        ('indicators', {
            'CumulativeTick': {
                'class': CumulativeTick,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CumulativeTick'>
            },
            'CCITurbo': {
                'class': CCITurbo,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CCITurbo'>
            }
        }),
        ('weights', {
            'CumulativeTick': 1.0,
            'CCITurbo': 1.0
        })
    )
