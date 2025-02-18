import backtrader as bt
from ..base_strategy import FlexibleStrategy

class EldersForceIndex_MarketBalance_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von EldersForceIndex und MarketBalance
    """
    
    params = (
        ('indicators', {
            'EldersForceIndex': {
                'class': EldersForceIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EldersForceIndex'>
            },
            'MarketBalance': {
                'class': MarketBalance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketBalance'>
            }
        }),
        ('weights', {
            'EldersForceIndex': 1.0,
            'MarketBalance': 1.0
        })
    )
