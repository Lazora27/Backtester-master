import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PVINVIComparison_DemandSupplyIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PVINVIComparison und DemandSupplyIndex
    """
    
    params = (
        ('indicators', {
            'PVINVIComparison': {
                'class': PVINVIComparison,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PVINVIComparison'>
            },
            'DemandSupplyIndex': {
                'class': DemandSupplyIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandSupplyIndex'>
            }
        }),
        ('weights', {
            'PVINVIComparison': 1.0,
            'DemandSupplyIndex': 1.0
        })
    )
