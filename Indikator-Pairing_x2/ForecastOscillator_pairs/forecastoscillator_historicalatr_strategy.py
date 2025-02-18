import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ForecastOscillator_HistoricalATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ForecastOscillator und HistoricalATR
    """
    
    params = (
        ('indicators', {
            'ForecastOscillator': {
                'class': ForecastOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ForecastOscillator'>
            },
            'HistoricalATR': {
                'class': HistoricalATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalATR'>
            }
        }),
        ('weights', {
            'ForecastOscillator': 1.0,
            'HistoricalATR': 1.0
        })
    )
