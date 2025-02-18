import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SupplyDemandZones_ExponentialMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SupplyDemandZones und ExponentialMovingAverage
    """
    
    params = (
        ('indicators', {
            'SupplyDemandZones': {
                'class': SupplyDemandZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SupplyDemandZones'>
            },
            'ExponentialMovingAverage': {
                'class': ExponentialMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExponentialMovingAverage'>
            }
        }),
        ('weights', {
            'SupplyDemandZones': 1.0,
            'ExponentialMovingAverage': 1.0
        })
    )
