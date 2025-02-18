import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TimeSeriesForecast_BradleySiderograph_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TimeSeriesForecast und BradleySiderograph
    """
    
    params = (
        ('indicators', {
            'TimeSeriesForecast': {
                'class': TimeSeriesForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSeriesForecast'>
            },
            'BradleySiderograph': {
                'class': BradleySiderograph,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BradleySiderograph'>
            }
        }),
        ('weights', {
            'TimeSeriesForecast': 1.0,
            'BradleySiderograph': 1.0
        })
    )
