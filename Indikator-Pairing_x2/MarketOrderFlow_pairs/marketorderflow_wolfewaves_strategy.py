import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketOrderFlow_WolfeWaves_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketOrderFlow und WolfeWaves
    """
    
    params = (
        ('indicators', {
            'MarketOrderFlow': {
                'class': MarketOrderFlow,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketOrderFlow'>
            },
            'WolfeWaves': {
                'class': WolfeWaves,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaves'>
            }
        }),
        ('weights', {
            'MarketOrderFlow': 1.0,
            'WolfeWaves': 1.0
        })
    )
