import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CumulativeTick_AverageTrueRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CumulativeTick und AverageTrueRange
    """
    
    params = (
        ('indicators', {
            'CumulativeTick': {
                'class': CumulativeTick,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CumulativeTick'>
            },
            'AverageTrueRange': {
                'class': AverageTrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageTrueRange1'>
            }
        }),
        ('weights', {
            'CumulativeTick': 1.0,
            'AverageTrueRange': 1.0
        })
    )
