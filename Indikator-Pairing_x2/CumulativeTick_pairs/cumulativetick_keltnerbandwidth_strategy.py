import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CumulativeTick_KeltnerBandWidth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CumulativeTick und KeltnerBandWidth
    """
    
    params = (
        ('indicators', {
            'CumulativeTick': {
                'class': CumulativeTick,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CumulativeTick'>
            },
            'KeltnerBandWidth': {
                'class': KeltnerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerBandWidth'>
            }
        }),
        ('weights', {
            'CumulativeTick': 1.0,
            'KeltnerBandWidth': 1.0
        })
    )
