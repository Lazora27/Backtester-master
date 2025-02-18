import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MLForecast_TapeReading_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MLForecast und TapeReading
    """
    
    params = (
        ('indicators', {
            'MLForecast': {
                'class': MLForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MLForecast'>
            },
            'TapeReading': {
                'class': TapeReading,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TapeReading'>
            }
        }),
        ('weights', {
            'MLForecast': 1.0,
            'TapeReading': 1.0
        })
    )
