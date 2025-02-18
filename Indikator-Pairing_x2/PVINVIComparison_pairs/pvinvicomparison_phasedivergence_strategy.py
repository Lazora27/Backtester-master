import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PVINVIComparison_PhaseDivergence_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PVINVIComparison und PhaseDivergence
    """
    
    params = (
        ('indicators', {
            'PVINVIComparison': {
                'class': PVINVIComparison,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PVINVIComparison'>
            },
            'PhaseDivergence': {
                'class': PhaseDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PhaseDivergence'>
            }
        }),
        ('weights', {
            'PVINVIComparison': 1.0,
            'PhaseDivergence': 1.0
        })
    )
