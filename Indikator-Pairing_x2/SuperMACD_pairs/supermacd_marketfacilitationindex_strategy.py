import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SuperMACD_MarketFacilitationIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SuperMACD und MarketFacilitationIndex
    """
    
    params = (
        ('indicators', {
            'SuperMACD': {
                'class': SuperMACD,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperMACD'>
            },
            'MarketFacilitationIndex': {
                'class': MarketFacilitationIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketFacilitationIndex'>
            }
        }),
        ('weights', {
            'SuperMACD': 1.0,
            'MarketFacilitationIndex': 1.0
        })
    )
