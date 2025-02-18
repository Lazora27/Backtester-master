import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FisherTransform_ForecastOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FisherTransform und ForecastOscillator
    """
    
    params = (
        ('indicators', {
            'FisherTransform': {
                'class': FisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherTransform'>
            },
            'ForecastOscillator': {
                'class': ForecastOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ForecastOscillator'>
            }
        }),
        ('weights', {
            'FisherTransform': 1.0,
            'ForecastOscillator': 1.0
        })
    )
