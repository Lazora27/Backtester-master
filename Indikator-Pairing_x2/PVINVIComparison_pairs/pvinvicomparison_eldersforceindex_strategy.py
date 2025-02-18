import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PVINVIComparison_EldersForceIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PVINVIComparison und EldersForceIndex
    """
    
    params = (
        ('indicators', {
            'PVINVIComparison': {
                'class': PVINVIComparison,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PVINVIComparison'>
            },
            'EldersForceIndex': {
                'class': EldersForceIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EldersForceIndex'>
            }
        }),
        ('weights', {
            'PVINVIComparison': 1.0,
            'EldersForceIndex': 1.0
        })
    )
