import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketBalance_MarketFacilitationIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketBalance und MarketFacilitationIndex
    """
    
    params = (
        ('indicators', {
            'MarketBalance': {
                'class': MarketBalance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketBalance'>
            },
            'MarketFacilitationIndex': {
                'class': MarketFacilitationIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketFacilitationIndex'>
            }
        }),
        ('weights', {
            'MarketBalance': 1.0,
            'MarketFacilitationIndex': 1.0
        })
    )
