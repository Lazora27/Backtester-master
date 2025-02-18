import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketOrderFlow_GannFans_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketOrderFlow und GannFans
    """
    
    params = (
        ('indicators', {
            'MarketOrderFlow': {
                'class': MarketOrderFlow,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketOrderFlow'>
            },
            'GannFans': {
                'class': GannFans,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannFans'>
            }
        }),
        ('weights', {
            'MarketOrderFlow': 1.0,
            'GannFans': 1.0
        })
    )
