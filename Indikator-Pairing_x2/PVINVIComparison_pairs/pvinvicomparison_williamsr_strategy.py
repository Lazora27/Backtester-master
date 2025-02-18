import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PVINVIComparison_WilliamsR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PVINVIComparison und WilliamsR
    """
    
    params = (
        ('indicators', {
            'PVINVIComparison': {
                'class': PVINVIComparison,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PVINVIComparison'>
            },
            'WilliamsR': {
                'class': WilliamsR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsR1'>
            }
        }),
        ('weights', {
            'PVINVIComparison': 1.0,
            'WilliamsR': 1.0
        })
    )
