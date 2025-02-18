import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MLForecast_RateOfChange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MLForecast und RateOfChange
    """
    
    params = (
        ('indicators', {
            'MLForecast': {
                'class': MLForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MLForecast'>
            },
            'RateOfChange': {
                'class': RateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RateOfChange1'>
            }
        }),
        ('weights', {
            'MLForecast': 1.0,
            'RateOfChange': 1.0
        })
    )
