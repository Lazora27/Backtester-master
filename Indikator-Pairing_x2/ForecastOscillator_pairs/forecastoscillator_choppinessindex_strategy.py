import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ForecastOscillator_ChoppinessIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ForecastOscillator und ChoppinessIndex
    """
    
    params = (
        ('indicators', {
            'ForecastOscillator': {
                'class': ForecastOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ForecastOscillator'>
            },
            'ChoppinessIndex': {
                'class': ChoppinessIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChoppinessIndex'>
            }
        }),
        ('weights', {
            'ForecastOscillator': 1.0,
            'ChoppinessIndex': 1.0
        })
    )
