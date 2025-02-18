import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketBalance_DemandIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketBalance und DemandIndex
    """
    
    params = (
        ('indicators', {
            'MarketBalance': {
                'class': MarketBalance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketBalance'>
            },
            'DemandIndex': {
                'class': DemandIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandIndex'>
            }
        }),
        ('weights', {
            'MarketBalance': 1.0,
            'DemandIndex': 1.0
        })
    )
