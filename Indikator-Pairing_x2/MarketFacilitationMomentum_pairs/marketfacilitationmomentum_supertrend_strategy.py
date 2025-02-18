import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketFacilitationMomentum_SuperTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketFacilitationMomentum und SuperTrend
    """
    
    params = (
        ('indicators', {
            'MarketFacilitationMomentum': {
                'class': MarketFacilitationMomentum,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketFacilitationMomentum'>
            },
            'SuperTrend': {
                'class': SuperTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperTrend'>
            }
        }),
        ('weights', {
            'MarketFacilitationMomentum': 1.0,
            'SuperTrend': 1.0
        })
    )
