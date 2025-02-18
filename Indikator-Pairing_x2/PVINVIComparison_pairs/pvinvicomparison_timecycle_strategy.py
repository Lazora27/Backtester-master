import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PVINVIComparison_TimeCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PVINVIComparison und TimeCycle
    """
    
    params = (
        ('indicators', {
            'PVINVIComparison': {
                'class': PVINVIComparison,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PVINVIComparison'>
            },
            'TimeCycle': {
                'class': TimeCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeCycle'>
            }
        }),
        ('weights', {
            'PVINVIComparison': 1.0,
            'TimeCycle': 1.0
        })
    )
