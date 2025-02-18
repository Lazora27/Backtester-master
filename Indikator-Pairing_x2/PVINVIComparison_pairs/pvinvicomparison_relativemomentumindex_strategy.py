import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PVINVIComparison_RelativeMomentumIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PVINVIComparison und RelativeMomentumIndex
    """
    
    params = (
        ('indicators', {
            'PVINVIComparison': {
                'class': PVINVIComparison,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PVINVIComparison'>
            },
            'RelativeMomentumIndex': {
                'class': RelativeMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeMomentumIndex'>
            }
        }),
        ('weights', {
            'PVINVIComparison': 1.0,
            'RelativeMomentumIndex': 1.0
        })
    )
