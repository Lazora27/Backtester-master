import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AwesomeOscillator_MarketOrderFlow_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AwesomeOscillator und MarketOrderFlow
    """
    
    params = (
        ('indicators', {
            'AwesomeOscillator': {
                'class': AwesomeOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AwesomeOscillator1'>
            },
            'MarketOrderFlow': {
                'class': MarketOrderFlow,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketOrderFlow'>
            }
        }),
        ('weights', {
            'AwesomeOscillator': 1.0,
            'MarketOrderFlow': 1.0
        })
    )
