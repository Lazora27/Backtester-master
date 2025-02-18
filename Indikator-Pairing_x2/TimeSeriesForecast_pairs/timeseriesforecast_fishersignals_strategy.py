import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TimeSeriesForecast_FisherSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TimeSeriesForecast und FisherSignals
    """
    
    params = (
        ('indicators', {
            'TimeSeriesForecast': {
                'class': TimeSeriesForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSeriesForecast'>
            },
            'FisherSignals': {
                'class': FisherSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherSignals'>
            }
        }),
        ('weights', {
            'TimeSeriesForecast': 1.0,
            'FisherSignals': 1.0
        })
    )
