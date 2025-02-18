import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TimeSeriesForecast_SupplyDemandZones_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TimeSeriesForecast und SupplyDemandZones
    """
    
    params = (
        ('indicators', {
            'TimeSeriesForecast': {
                'class': TimeSeriesForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSeriesForecast'>
            },
            'SupplyDemandZones': {
                'class': SupplyDemandZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SupplyDemandZones'>
            }
        }),
        ('weights', {
            'TimeSeriesForecast': 1.0,
            'SupplyDemandZones': 1.0
        })
    )
