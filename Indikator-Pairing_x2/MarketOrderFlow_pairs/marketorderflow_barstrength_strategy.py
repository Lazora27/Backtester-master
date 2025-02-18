import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketOrderFlow_BarStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketOrderFlow und BarStrength
    """
    
    params = (
        ('indicators', {
            'MarketOrderFlow': {
                'class': MarketOrderFlow,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketOrderFlow'>
            },
            'BarStrength': {
                'class': BarStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BarStrength'>
            }
        }),
        ('weights', {
            'MarketOrderFlow': 1.0,
            'BarStrength': 1.0
        })
    )
