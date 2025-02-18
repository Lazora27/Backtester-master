import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ForecastOscillator_BradleySiderograph_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ForecastOscillator und BradleySiderograph
    """
    
    params = (
        ('indicators', {
            'ForecastOscillator': {
                'class': ForecastOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ForecastOscillator'>
            },
            'BradleySiderograph': {
                'class': BradleySiderograph,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BradleySiderograph'>
            }
        }),
        ('weights', {
            'ForecastOscillator': 1.0,
            'BradleySiderograph': 1.0
        })
    )
