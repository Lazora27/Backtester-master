import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChaikinOscillator_MarketOrderFlow_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChaikinOscillator und MarketOrderFlow
    """
    
    params = (
        ('indicators', {
            'ChaikinOscillator': {
                'class': ChaikinOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinOscillator'>
            },
            'MarketOrderFlow': {
                'class': MarketOrderFlow,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketOrderFlow'>
            }
        }),
        ('weights', {
            'ChaikinOscillator': 1.0,
            'MarketOrderFlow': 1.0
        })
    )
