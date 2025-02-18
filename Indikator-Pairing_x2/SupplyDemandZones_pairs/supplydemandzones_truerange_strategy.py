import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SupplyDemandZones_TrueRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SupplyDemandZones und TrueRange
    """
    
    params = (
        ('indicators', {
            'SupplyDemandZones': {
                'class': SupplyDemandZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SupplyDemandZones'>
            },
            'TrueRange': {
                'class': TrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRange1'>
            }
        }),
        ('weights', {
            'SupplyDemandZones': 1.0,
            'TrueRange': 1.0
        })
    )
