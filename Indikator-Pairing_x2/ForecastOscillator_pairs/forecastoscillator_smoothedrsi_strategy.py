import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ForecastOscillator_SmoothedRSI_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ForecastOscillator und SmoothedRSI
    """
    
    params = (
        ('indicators', {
            'ForecastOscillator': {
                'class': ForecastOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ForecastOscillator'>
            },
            'SmoothedRSI': {
                'class': SmoothedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedRSI'>
            }
        }),
        ('weights', {
            'ForecastOscillator': 1.0,
            'SmoothedRSI': 1.0
        })
    )
