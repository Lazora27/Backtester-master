import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceVolumeTrend_SmoothedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceVolumeTrend und SmoothedCycle
    """
    
    params = (
        ('indicators', {
            'PriceVolumeTrend': {
                'class': PriceVolumeTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceVolumeTrend'>
            },
            'SmoothedCycle': {
                'class': SmoothedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedCycle'>
            }
        }),
        ('weights', {
            'PriceVolumeTrend': 1.0,
            'SmoothedCycle': 1.0
        })
    )
