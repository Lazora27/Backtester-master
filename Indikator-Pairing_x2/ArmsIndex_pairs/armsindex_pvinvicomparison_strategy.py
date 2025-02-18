import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ArmsIndex_PVINVIComparison_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ArmsIndex und PVINVIComparison
    """
    
    params = (
        ('indicators', {
            'ArmsIndex': {
                'class': ArmsIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ArmsIndex'>
            },
            'PVINVIComparison': {
                'class': PVINVIComparison,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PVINVIComparison'>
            }
        }),
        ('weights', {
            'ArmsIndex': 1.0,
            'PVINVIComparison': 1.0
        })
    )
