import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ForecastOscillator_PriceSquawk_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ForecastOscillator und PriceSquawk
    """
    
    params = (
        ('indicators', {
            'ForecastOscillator': {
                'class': ForecastOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ForecastOscillator'>
            },
            'PriceSquawk': {
                'class': PriceSquawk,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceSquawk'>
            }
        }),
        ('weights', {
            'ForecastOscillator': 1.0,
            'PriceSquawk': 1.0
        })
    )
