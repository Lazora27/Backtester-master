import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ForecastOscillator_UlcerIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ForecastOscillator und UlcerIndex
    """
    
    params = (
        ('indicators', {
            'ForecastOscillator': {
                'class': ForecastOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ForecastOscillator'>
            },
            'UlcerIndex': {
                'class': UlcerIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndex'>
            }
        }),
        ('weights', {
            'ForecastOscillator': 1.0,
            'UlcerIndex': 1.0
        })
    )
