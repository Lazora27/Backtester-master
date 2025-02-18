import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PVINVIComparison_RelativeVigorIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PVINVIComparison und RelativeVigorIndex
    """
    
    params = (
        ('indicators', {
            'PVINVIComparison': {
                'class': PVINVIComparison,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PVINVIComparison'>
            },
            'RelativeVigorIndex': {
                'class': RelativeVigorIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeVigorIndex'>
            }
        }),
        ('weights', {
            'PVINVIComparison': 1.0,
            'RelativeVigorIndex': 1.0
        })
    )
