import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MLForecast_UltimateOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MLForecast und UltimateOscillator
    """
    
    params = (
        ('indicators', {
            'MLForecast': {
                'class': MLForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MLForecast'>
            },
            'UltimateOscillator': {
                'class': UltimateOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UltimateOscillator1'>
            }
        }),
        ('weights', {
            'MLForecast': 1.0,
            'UltimateOscillator': 1.0
        })
    )
