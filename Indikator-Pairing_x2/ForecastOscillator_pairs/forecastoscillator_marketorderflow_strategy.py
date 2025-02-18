import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ForecastOscillator_MarketOrderFlow_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ForecastOscillator und MarketOrderFlow
    """
    
    params = (
        ('indicators', {
            'ForecastOscillator': {
                'class': ForecastOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ForecastOscillator'>
            },
            'MarketOrderFlow': {
                'class': MarketOrderFlow,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketOrderFlow'>
            }
        }),
        ('weights', {
            'ForecastOscillator': 1.0,
            'MarketOrderFlow': 1.0
        })
    )
