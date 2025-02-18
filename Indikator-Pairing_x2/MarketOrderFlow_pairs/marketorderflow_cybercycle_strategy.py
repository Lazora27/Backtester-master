import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketOrderFlow_CyberCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketOrderFlow und CyberCycle
    """
    
    params = (
        ('indicators', {
            'MarketOrderFlow': {
                'class': MarketOrderFlow,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketOrderFlow'>
            },
            'CyberCycle': {
                'class': CyberCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycle'>
            }
        }),
        ('weights', {
            'MarketOrderFlow': 1.0,
            'CyberCycle': 1.0
        })
    )
