import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ForecastOscillator_DetrendedPriceIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ForecastOscillator und DetrendedPriceIndicator
    """
    
    params = (
        ('indicators', {
            'ForecastOscillator': {
                'class': ForecastOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ForecastOscillator'>
            },
            'DetrendedPriceIndicator': {
                'class': DetrendedPriceIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DetrendedPriceIndicator'>
            }
        }),
        ('weights', {
            'ForecastOscillator': 1.0,
            'DetrendedPriceIndicator': 1.0
        })
    )
