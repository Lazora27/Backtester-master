import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PVINVIComparison_CenterOfGravity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PVINVIComparison und CenterOfGravity
    """
    
    params = (
        ('indicators', {
            'PVINVIComparison': {
                'class': PVINVIComparison,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PVINVIComparison'>
            },
            'CenterOfGravity': {
                'class': CenterOfGravity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CenterOfGravity'>
            }
        }),
        ('weights', {
            'PVINVIComparison': 1.0,
            'CenterOfGravity': 1.0
        })
    )
