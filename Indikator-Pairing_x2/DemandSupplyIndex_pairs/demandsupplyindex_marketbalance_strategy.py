import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DemandSupplyIndex_MarketBalance_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DemandSupplyIndex und MarketBalance
    """
    
    params = (
        ('indicators', {
            'DemandSupplyIndex': {
                'class': DemandSupplyIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandSupplyIndex'>
            },
            'MarketBalance': {
                'class': MarketBalance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketBalance'>
            }
        }),
        ('weights', {
            'DemandSupplyIndex': 1.0,
            'MarketBalance': 1.0
        })
    )
