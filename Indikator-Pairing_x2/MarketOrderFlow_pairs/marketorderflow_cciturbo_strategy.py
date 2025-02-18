import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketOrderFlow_CCITurbo_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketOrderFlow und CCITurbo
    """
    
    params = (
        ('indicators', {
            'MarketOrderFlow': {
                'class': MarketOrderFlow,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketOrderFlow'>
            },
            'CCITurbo': {
                'class': CCITurbo,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CCITurbo'>
            }
        }),
        ('weights', {
            'MarketOrderFlow': 1.0,
            'CCITurbo': 1.0
        })
    )
