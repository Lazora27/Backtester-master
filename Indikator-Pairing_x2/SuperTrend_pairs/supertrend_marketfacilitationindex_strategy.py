import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SuperTrend_MarketFacilitationIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SuperTrend und MarketFacilitationIndex
    """
    
    params = (
        ('indicators', {
            'SuperTrend': {
                'class': SuperTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperTrend'>
            },
            'MarketFacilitationIndex': {
                'class': MarketFacilitationIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketFacilitationIndex'>
            }
        }),
        ('weights', {
            'SuperTrend': 1.0,
            'MarketFacilitationIndex': 1.0
        })
    )
