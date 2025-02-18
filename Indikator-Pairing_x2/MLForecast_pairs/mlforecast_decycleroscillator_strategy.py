import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MLForecast_DecyclerOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MLForecast und DecyclerOscillator
    """
    
    params = (
        ('indicators', {
            'MLForecast': {
                'class': MLForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MLForecast'>
            },
            'DecyclerOscillator': {
                'class': DecyclerOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DecyclerOscillator'>
            }
        }),
        ('weights', {
            'MLForecast': 1.0,
            'DecyclerOscillator': 1.0
        })
    )
