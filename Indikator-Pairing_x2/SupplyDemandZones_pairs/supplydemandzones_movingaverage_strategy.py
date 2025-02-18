import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SupplyDemandZones_MovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SupplyDemandZones und MovingAverage
    """
    
    params = (
        ('indicators', {
            'SupplyDemandZones': {
                'class': SupplyDemandZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SupplyDemandZones'>
            },
            'MovingAverage': {
                'class': MovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MovingAverage'>
            }
        }),
        ('weights', {
            'SupplyDemandZones': 1.0,
            'MovingAverage': 1.0
        })
    )
