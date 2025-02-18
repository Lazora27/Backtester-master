import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HeikenAshiTrend_SmoothedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HeikenAshiTrend und SmoothedCycle
    """
    
    params = (
        ('indicators', {
            'HeikenAshiTrend': {
                'class': HeikenAshiTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HeikenAshiTrend'>
            },
            'SmoothedCycle': {
                'class': SmoothedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedCycle'>
            }
        }),
        ('weights', {
            'HeikenAshiTrend': 1.0,
            'SmoothedCycle': 1.0
        })
    )
