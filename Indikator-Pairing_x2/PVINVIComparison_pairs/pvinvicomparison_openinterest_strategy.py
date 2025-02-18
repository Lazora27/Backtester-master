import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PVINVIComparison_OpenInterest_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PVINVIComparison und OpenInterest
    """
    
    params = (
        ('indicators', {
            'PVINVIComparison': {
                'class': PVINVIComparison,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PVINVIComparison'>
            },
            'OpenInterest': {
                'class': OpenInterest,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OpenInterest'>
            }
        }),
        ('weights', {
            'PVINVIComparison': 1.0,
            'OpenInterest': 1.0
        })
    )
