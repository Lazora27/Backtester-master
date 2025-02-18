import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CumulativeTick_SharpeRatioIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CumulativeTick und SharpeRatioIndicator
    """
    
    params = (
        ('indicators', {
            'CumulativeTick': {
                'class': CumulativeTick,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CumulativeTick'>
            },
            'SharpeRatioIndicator': {
                'class': SharpeRatioIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SharpeRatioIndicator'>
            }
        }),
        ('weights', {
            'CumulativeTick': 1.0,
            'SharpeRatioIndicator': 1.0
        })
    )
