import backtrader as bt
from ..base_strategy import FlexibleStrategy

class EldersForceIndex_MarketOrderFlow_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von EldersForceIndex und MarketOrderFlow
    """
    
    params = (
        ('indicators', {
            'EldersForceIndex': {
                'class': EldersForceIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EldersForceIndex'>
            },
            'MarketOrderFlow': {
                'class': MarketOrderFlow,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketOrderFlow'>
            }
        }),
        ('weights', {
            'EldersForceIndex': 1.0,
            'MarketOrderFlow': 1.0
        })
    )
