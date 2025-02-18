import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrendExhaustion_HeikenAshiTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrendExhaustion und HeikenAshiTrend
    """
    
    params = (
        ('indicators', {
            'TrendExhaustion': {
                'class': TrendExhaustion,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendExhaustion'>
            },
            'HeikenAshiTrend': {
                'class': HeikenAshiTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HeikenAshiTrend'>
            }
        }),
        ('weights', {
            'TrendExhaustion': 1.0,
            'HeikenAshiTrend': 1.0
        })
    )
