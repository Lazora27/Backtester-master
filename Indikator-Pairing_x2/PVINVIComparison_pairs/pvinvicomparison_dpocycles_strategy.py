import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PVINVIComparison_DPOCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PVINVIComparison und DPOCycles
    """
    
    params = (
        ('indicators', {
            'PVINVIComparison': {
                'class': PVINVIComparison,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PVINVIComparison'>
            },
            'DPOCycles': {
                'class': DPOCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DPOCycles'>
            }
        }),
        ('weights', {
            'PVINVIComparison': 1.0,
            'DPOCycles': 1.0
        })
    )
