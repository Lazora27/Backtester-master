import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceVolumeTrend_WeightedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceVolumeTrend und WeightedCycle
    """
    
    params = (
        ('indicators', {
            'PriceVolumeTrend': {
                'class': PriceVolumeTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceVolumeTrend'>
            },
            'WeightedCycle': {
                'class': WeightedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedCycle'>
            }
        }),
        ('weights', {
            'PriceVolumeTrend': 1.0,
            'WeightedCycle': 1.0
        })
    )
