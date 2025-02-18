import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceDelta_MarketFacilitationIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceDelta und MarketFacilitationIndex
    """
    
    params = (
        ('indicators', {
            'PriceDelta': {
                'class': PriceDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceDelta'>
            },
            'MarketFacilitationIndex': {
                'class': MarketFacilitationIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketFacilitationIndex'>
            }
        }),
        ('weights', {
            'PriceDelta': 1.0,
            'MarketFacilitationIndex': 1.0
        })
    )
