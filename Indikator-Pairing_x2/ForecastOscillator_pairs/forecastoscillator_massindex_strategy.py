import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ForecastOscillator_MassIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ForecastOscillator und MassIndex
    """
    
    params = (
        ('indicators', {
            'ForecastOscillator': {
                'class': ForecastOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ForecastOscillator'>
            },
            'MassIndex': {
                'class': MassIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MassIndex'>
            }
        }),
        ('weights', {
            'ForecastOscillator': 1.0,
            'MassIndex': 1.0
        })
    )
