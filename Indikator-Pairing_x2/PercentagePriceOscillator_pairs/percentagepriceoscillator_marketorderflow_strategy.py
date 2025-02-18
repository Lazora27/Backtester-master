import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PercentagePriceOscillator_MarketOrderFlow_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PercentagePriceOscillator und MarketOrderFlow
    """
    
    params = (
        ('indicators', {
            'PercentagePriceOscillator': {
                'class': PercentagePriceOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PercentagePriceOscillator'>
            },
            'MarketOrderFlow': {
                'class': MarketOrderFlow,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketOrderFlow'>
            }
        }),
        ('weights', {
            'PercentagePriceOscillator': 1.0,
            'MarketOrderFlow': 1.0
        })
    )
