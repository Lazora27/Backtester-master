import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PVINVIComparison_DemandIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PVINVIComparison und DemandIndex
    """
    
    params = (
        ('indicators', {
            'PVINVIComparison': {
                'class': PVINVIComparison,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PVINVIComparison'>
            },
            'DemandIndex': {
                'class': DemandIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandIndex'>
            }
        }),
        ('weights', {
            'PVINVIComparison': 1.0,
            'DemandIndex': 1.0
        })
    )
