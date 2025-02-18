import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceVolumeTrend_MarketFacilitationIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceVolumeTrend und MarketFacilitationIndex
    """
    
    params = (
        ('indicators', {
            'PriceVolumeTrend': {
                'class': PriceVolumeTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceVolumeTrend'>
            },
            'MarketFacilitationIndex': {
                'class': MarketFacilitationIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketFacilitationIndex'>
            }
        }),
        ('weights', {
            'PriceVolumeTrend': 1.0,
            'MarketFacilitationIndex': 1.0
        })
    )
