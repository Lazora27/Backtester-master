import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ForecastOscillator_RateOfChange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ForecastOscillator und RateOfChange
    """
    
    params = (
        ('indicators', {
            'ForecastOscillator': {
                'class': ForecastOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ForecastOscillator'>
            },
            'RateOfChange': {
                'class': RateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RateOfChange1'>
            }
        }),
        ('weights', {
            'ForecastOscillator': 1.0,
            'RateOfChange': 1.0
        })
    )
