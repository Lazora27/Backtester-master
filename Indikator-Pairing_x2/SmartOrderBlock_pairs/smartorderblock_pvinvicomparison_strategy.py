import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmartOrderBlock_PVINVIComparison_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmartOrderBlock und PVINVIComparison
    """
    
    params = (
        ('indicators', {
            'SmartOrderBlock': {
                'class': SmartOrderBlock,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmartOrderBlock'>
            },
            'PVINVIComparison': {
                'class': PVINVIComparison,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PVINVIComparison'>
            }
        }),
        ('weights', {
            'SmartOrderBlock': 1.0,
            'PVINVIComparison': 1.0
        })
    )
