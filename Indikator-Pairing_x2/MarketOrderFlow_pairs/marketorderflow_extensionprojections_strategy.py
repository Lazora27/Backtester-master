import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketOrderFlow_ExtensionProjections_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketOrderFlow und ExtensionProjections
    """
    
    params = (
        ('indicators', {
            'MarketOrderFlow': {
                'class': MarketOrderFlow,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketOrderFlow'>
            },
            'ExtensionProjections': {
                'class': ExtensionProjections,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExtensionProjections'>
            }
        }),
        ('weights', {
            'MarketOrderFlow': 1.0,
            'ExtensionProjections': 1.0
        })
    )
