import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketOrderFlow_EhlersDecycler_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketOrderFlow und EhlersDecycler
    """
    
    params = (
        ('indicators', {
            'MarketOrderFlow': {
                'class': MarketOrderFlow,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketOrderFlow'>
            },
            'EhlersDecycler': {
                'class': EhlersDecycler,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersDecycler'>
            }
        }),
        ('weights', {
            'MarketOrderFlow': 1.0,
            'EhlersDecycler': 1.0
        })
    )
