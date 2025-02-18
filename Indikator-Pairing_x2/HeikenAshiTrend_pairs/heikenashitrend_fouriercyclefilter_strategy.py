import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HeikenAshiTrend_FourierCycleFilter_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HeikenAshiTrend und FourierCycleFilter
    """
    
    params = (
        ('indicators', {
            'HeikenAshiTrend': {
                'class': HeikenAshiTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HeikenAshiTrend'>
            },
            'FourierCycleFilter': {
                'class': FourierCycleFilter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierCycleFilter'>
            }
        }),
        ('weights', {
            'HeikenAshiTrend': 1.0,
            'FourierCycleFilter': 1.0
        })
    )
