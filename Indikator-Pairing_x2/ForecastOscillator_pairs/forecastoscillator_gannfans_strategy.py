import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ForecastOscillator_GannFans_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ForecastOscillator und GannFans
    """
    
    params = (
        ('indicators', {
            'ForecastOscillator': {
                'class': ForecastOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ForecastOscillator'>
            },
            'GannFans': {
                'class': GannFans,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannFans'>
            }
        }),
        ('weights', {
            'ForecastOscillator': 1.0,
            'GannFans': 1.0
        })
    )
