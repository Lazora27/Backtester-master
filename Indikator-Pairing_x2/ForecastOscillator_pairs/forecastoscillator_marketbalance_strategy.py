import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ForecastOscillator_MarketBalance_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ForecastOscillator und MarketBalance
    """
    
    params = (
        ('indicators', {
            'ForecastOscillator': {
                'class': ForecastOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ForecastOscillator'>
            },
            'MarketBalance': {
                'class': MarketBalance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketBalance'>
            }
        }),
        ('weights', {
            'ForecastOscillator': 1.0,
            'MarketBalance': 1.0
        })
    )
