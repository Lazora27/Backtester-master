import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ForecastOscillator_EhlersFisherTransform_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ForecastOscillator und EhlersFisherTransform
    """
    
    params = (
        ('indicators', {
            'ForecastOscillator': {
                'class': ForecastOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ForecastOscillator'>
            },
            'EhlersFisherTransform': {
                'class': EhlersFisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersFisherTransform'>
            }
        }),
        ('weights', {
            'ForecastOscillator': 1.0,
            'EhlersFisherTransform': 1.0
        })
    )
