import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ForecastOscillator_DeltaProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ForecastOscillator und DeltaProfile
    """
    
    params = (
        ('indicators', {
            'ForecastOscillator': {
                'class': ForecastOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ForecastOscillator'>
            },
            'DeltaProfile': {
                'class': DeltaProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DeltaProfile'>
            }
        }),
        ('weights', {
            'ForecastOscillator': 1.0,
            'DeltaProfile': 1.0
        })
    )
