import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HeikenAshiTrend_WeightedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HeikenAshiTrend und WeightedCycle
    """
    
    params = (
        ('indicators', {
            'HeikenAshiTrend': {
                'class': HeikenAshiTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HeikenAshiTrend'>
            },
            'WeightedCycle': {
                'class': WeightedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedCycle'>
            }
        }),
        ('weights', {
            'HeikenAshiTrend': 1.0,
            'WeightedCycle': 1.0
        })
    )
