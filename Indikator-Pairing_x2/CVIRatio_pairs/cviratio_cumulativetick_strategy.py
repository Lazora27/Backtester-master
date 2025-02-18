import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CVIRatio_CumulativeTick_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CVIRatio und CumulativeTick
    """
    
    params = (
        ('indicators', {
            'CVIRatio': {
                'class': CVIRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CVIRatio'>
            },
            'CumulativeTick': {
                'class': CumulativeTick,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CumulativeTick'>
            }
        }),
        ('weights', {
            'CVIRatio': 1.0,
            'CumulativeTick': 1.0
        })
    )
