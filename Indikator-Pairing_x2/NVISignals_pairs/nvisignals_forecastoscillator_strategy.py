import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NVISignals_ForecastOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NVISignals und ForecastOscillator
    """
    
    params = (
        ('indicators', {
            'NVISignals': {
                'class': NVISignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NVISignals'>
            },
            'ForecastOscillator': {
                'class': ForecastOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ForecastOscillator'>
            }
        }),
        ('weights', {
            'NVISignals': 1.0,
            'ForecastOscillator': 1.0
        })
    )
