import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TimeSeriesForecast_DPOCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TimeSeriesForecast und DPOCycles
    """
    
    params = (
        ('indicators', {
            'TimeSeriesForecast': {
                'class': TimeSeriesForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSeriesForecast'>
            },
            'DPOCycles': {
                'class': DPOCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DPOCycles'>
            }
        }),
        ('weights', {
            'TimeSeriesForecast': 1.0,
            'DPOCycles': 1.0
        })
    )
