import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TimeSeriesForecast_ParabolicSAR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TimeSeriesForecast und ParabolicSAR
    """
    
    params = (
        ('indicators', {
            'TimeSeriesForecast': {
                'class': TimeSeriesForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSeriesForecast'>
            },
            'ParabolicSAR': {
                'class': ParabolicSAR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicSAR'>
            }
        }),
        ('weights', {
            'TimeSeriesForecast': 1.0,
            'ParabolicSAR': 1.0
        })
    )
