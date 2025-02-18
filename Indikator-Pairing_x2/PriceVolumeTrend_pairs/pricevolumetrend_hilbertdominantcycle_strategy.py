import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceVolumeTrend_HilbertDominantCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceVolumeTrend und HilbertDominantCycle
    """
    
    params = (
        ('indicators', {
            'PriceVolumeTrend': {
                'class': PriceVolumeTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceVolumeTrend'>
            },
            'HilbertDominantCycle': {
                'class': HilbertDominantCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertDominantCycle'>
            }
        }),
        ('weights', {
            'PriceVolumeTrend': 1.0,
            'HilbertDominantCycle': 1.0
        })
    )
