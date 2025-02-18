import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MLForecast_SineWaveAdaptive_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MLForecast und SineWaveAdaptive
    """
    
    params = (
        ('indicators', {
            'MLForecast': {
                'class': MLForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MLForecast'>
            },
            'SineWaveAdaptive': {
                'class': SineWaveAdaptive,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveAdaptive'>
            }
        }),
        ('weights', {
            'MLForecast': 1.0,
            'SineWaveAdaptive': 1.0
        })
    )
