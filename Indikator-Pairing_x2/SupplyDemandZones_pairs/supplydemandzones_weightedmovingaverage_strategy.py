import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SupplyDemandZones_WeightedMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SupplyDemandZones und WeightedMovingAverage
    """
    
    params = (
        ('indicators', {
            'SupplyDemandZones': {
                'class': SupplyDemandZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SupplyDemandZones'>
            },
            'WeightedMovingAverage': {
                'class': WeightedMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedMovingAverage'>
            }
        }),
        ('weights', {
            'SupplyDemandZones': 1.0,
            'WeightedMovingAverage': 1.0
        })
    )
