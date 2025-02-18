import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RelativeVigorIndex_TimeSeriesForecast_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RelativeVigorIndex und TimeSeriesForecast
    """
    
    params = (
        ('indicators', {
            'RelativeVigorIndex': {
                'class': RelativeVigorIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeVigorIndex'>
            },
            'TimeSeriesForecast': {
                'class': TimeSeriesForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSeriesForecast'>
            }
        }),
        ('weights', {
            'RelativeVigorIndex': 1.0,
            'TimeSeriesForecast': 1.0
        })
    )
