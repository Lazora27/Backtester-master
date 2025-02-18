import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ForecastOscillator_TimeSalesVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ForecastOscillator und TimeSalesVolume
    """
    
    params = (
        ('indicators', {
            'ForecastOscillator': {
                'class': ForecastOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ForecastOscillator'>
            },
            'TimeSalesVolume': {
                'class': TimeSalesVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSalesVolume'>
            }
        }),
        ('weights', {
            'ForecastOscillator': 1.0,
            'TimeSalesVolume': 1.0
        })
    )
