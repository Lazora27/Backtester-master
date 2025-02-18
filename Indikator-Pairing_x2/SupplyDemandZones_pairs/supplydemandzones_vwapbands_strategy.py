import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SupplyDemandZones_VWAPBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SupplyDemandZones und VWAPBands
    """
    
    params = (
        ('indicators', {
            'SupplyDemandZones': {
                'class': SupplyDemandZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SupplyDemandZones'>
            },
            'VWAPBands': {
                'class': VWAPBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPBands'>
            }
        }),
        ('weights', {
            'SupplyDemandZones': 1.0,
            'VWAPBands': 1.0
        })
    )
