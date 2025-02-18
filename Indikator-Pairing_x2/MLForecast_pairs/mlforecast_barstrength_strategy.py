import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MLForecast_BarStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MLForecast und BarStrength
    """
    
    params = (
        ('indicators', {
            'MLForecast': {
                'class': MLForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MLForecast'>
            },
            'BarStrength': {
                'class': BarStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BarStrength'>
            }
        }),
        ('weights', {
            'MLForecast': 1.0,
            'BarStrength': 1.0
        })
    )
