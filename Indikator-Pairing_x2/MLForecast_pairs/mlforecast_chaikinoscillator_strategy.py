import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MLForecast_ChaikinOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MLForecast und ChaikinOscillator
    """
    
    params = (
        ('indicators', {
            'MLForecast': {
                'class': MLForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MLForecast'>
            },
            'ChaikinOscillator': {
                'class': ChaikinOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinOscillator'>
            }
        }),
        ('weights', {
            'MLForecast': 1.0,
            'ChaikinOscillator': 1.0
        })
    )
