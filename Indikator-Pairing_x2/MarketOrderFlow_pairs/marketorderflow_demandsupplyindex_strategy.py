import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketOrderFlow_DemandSupplyIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketOrderFlow und DemandSupplyIndex
    """
    
    params = (
        ('indicators', {
            'MarketOrderFlow': {
                'class': MarketOrderFlow,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketOrderFlow'>
            },
            'DemandSupplyIndex': {
                'class': DemandSupplyIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandSupplyIndex'>
            }
        }),
        ('weights', {
            'MarketOrderFlow': 1.0,
            'DemandSupplyIndex': 1.0
        })
    )
