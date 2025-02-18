import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PVINVIComparison_TickIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PVINVIComparison und TickIndex
    """
    
    params = (
        ('indicators', {
            'PVINVIComparison': {
                'class': PVINVIComparison,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PVINVIComparison'>
            },
            'TickIndex': {
                'class': TickIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickIndex'>
            }
        }),
        ('weights', {
            'PVINVIComparison': 1.0,
            'TickIndex': 1.0
        })
    )
