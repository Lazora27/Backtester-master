import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TimeSeriesForecast_AccumulationDistributionLine_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TimeSeriesForecast und AccumulationDistributionLine
    """
    
    params = (
        ('indicators', {
            'TimeSeriesForecast': {
                'class': TimeSeriesForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSeriesForecast'>
            },
            'AccumulationDistributionLine': {
                'class': AccumulationDistributionLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccumulationDistributionLine'>
            }
        }),
        ('weights', {
            'TimeSeriesForecast': 1.0,
            'AccumulationDistributionLine': 1.0
        })
    )
