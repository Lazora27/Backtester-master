import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketCycleIndicator_DemandSupplyIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketCycleIndicator und DemandSupplyIndex
    """
    
    params = (
        ('indicators', {
            'MarketCycleIndicator': {
                'class': MarketCycleIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketCycleIndicator'>
            },
            'DemandSupplyIndex': {
                'class': DemandSupplyIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandSupplyIndex'>
            }
        }),
        ('weights', {
            'MarketCycleIndicator': 1.0,
            'DemandSupplyIndex': 1.0
        })
    )
