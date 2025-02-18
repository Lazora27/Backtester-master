import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PVINVIComparison_SupplyDemandZones_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PVINVIComparison und SupplyDemandZones
    """
    
    params = (
        ('indicators', {
            'PVINVIComparison': {
                'class': PVINVIComparison,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PVINVIComparison'>
            },
            'SupplyDemandZones': {
                'class': SupplyDemandZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SupplyDemandZones'>
            }
        }),
        ('weights', {
            'PVINVIComparison': 1.0,
            'SupplyDemandZones': 1.0
        })
    )
