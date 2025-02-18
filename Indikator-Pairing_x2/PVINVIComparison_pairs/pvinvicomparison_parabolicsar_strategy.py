import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PVINVIComparison_ParabolicSAR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PVINVIComparison und ParabolicSAR
    """
    
    params = (
        ('indicators', {
            'PVINVIComparison': {
                'class': PVINVIComparison,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PVINVIComparison'>
            },
            'ParabolicSAR': {
                'class': ParabolicSAR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicSAR'>
            }
        }),
        ('weights', {
            'PVINVIComparison': 1.0,
            'ParabolicSAR': 1.0
        })
    )
