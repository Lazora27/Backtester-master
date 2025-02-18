import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketOrderFlow_ParabolicSAR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketOrderFlow und ParabolicSAR
    """
    
    params = (
        ('indicators', {
            'MarketOrderFlow': {
                'class': MarketOrderFlow,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketOrderFlow'>
            },
            'ParabolicSAR': {
                'class': ParabolicSAR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicSAR'>
            }
        }),
        ('weights', {
            'MarketOrderFlow': 1.0,
            'ParabolicSAR': 1.0
        })
    )
