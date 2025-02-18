import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PVINVIComparison_RelativeStrengthIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PVINVIComparison und RelativeStrengthIndex
    """
    
    params = (
        ('indicators', {
            'PVINVIComparison': {
                'class': PVINVIComparison,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PVINVIComparison'>
            },
            'RelativeStrengthIndex': {
                'class': RelativeStrengthIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeStrengthIndex1'>
            }
        }),
        ('weights', {
            'PVINVIComparison': 1.0,
            'RelativeStrengthIndex': 1.0
        })
    )
