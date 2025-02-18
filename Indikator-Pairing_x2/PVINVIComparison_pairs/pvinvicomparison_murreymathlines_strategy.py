import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PVINVIComparison_MurreyMathLines_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PVINVIComparison und MurreyMathLines
    """
    
    params = (
        ('indicators', {
            'PVINVIComparison': {
                'class': PVINVIComparison,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PVINVIComparison'>
            },
            'MurreyMathLines': {
                'class': MurreyMathLines,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathLines'>
            }
        }),
        ('weights', {
            'PVINVIComparison': 1.0,
            'MurreyMathLines': 1.0
        })
    )
