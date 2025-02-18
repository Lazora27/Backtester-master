import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsR_HeikenAshiTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsR und HeikenAshiTrend
    """
    
    params = (
        ('indicators', {
            'WilliamsR': {
                'class': WilliamsR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsR1'>
            },
            'HeikenAshiTrend': {
                'class': HeikenAshiTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HeikenAshiTrend'>
            }
        }),
        ('weights', {
            'WilliamsR': 1.0,
            'HeikenAshiTrend': 1.0
        })
    )
