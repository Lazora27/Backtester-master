import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ForecastOscillator_TwoPeriodRSI_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ForecastOscillator und TwoPeriodRSI
    """
    
    params = (
        ('indicators', {
            'ForecastOscillator': {
                'class': ForecastOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ForecastOscillator'>
            },
            'TwoPeriodRSI': {
                'class': TwoPeriodRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TwoPeriodRSI'>
            }
        }),
        ('weights', {
            'ForecastOscillator': 1.0,
            'TwoPeriodRSI': 1.0
        })
    )
