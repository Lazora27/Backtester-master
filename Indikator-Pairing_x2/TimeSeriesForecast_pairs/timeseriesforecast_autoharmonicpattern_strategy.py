import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TimeSeriesForecast_AutoHarmonicPattern_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TimeSeriesForecast und AutoHarmonicPattern
    """
    
    params = (
        ('indicators', {
            'TimeSeriesForecast': {
                'class': TimeSeriesForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSeriesForecast'>
            },
            'AutoHarmonicPattern': {
                'class': AutoHarmonicPattern,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoHarmonicPattern'>
            }
        }),
        ('weights', {
            'TimeSeriesForecast': 1.0,
            'AutoHarmonicPattern': 1.0
        })
    )
