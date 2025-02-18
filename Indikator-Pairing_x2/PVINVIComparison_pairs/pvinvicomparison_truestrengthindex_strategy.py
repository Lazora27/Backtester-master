import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PVINVIComparison_TrueStrengthIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PVINVIComparison und TrueStrengthIndex
    """
    
    params = (
        ('indicators', {
            'PVINVIComparison': {
                'class': PVINVIComparison,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PVINVIComparison'>
            },
            'TrueStrengthIndex': {
                'class': TrueStrengthIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueStrengthIndex'>
            }
        }),
        ('weights', {
            'PVINVIComparison': 1.0,
            'TrueStrengthIndex': 1.0
        })
    )
