import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PVINVIComparison_AccelerationBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PVINVIComparison und AccelerationBands
    """
    
    params = (
        ('indicators', {
            'PVINVIComparison': {
                'class': PVINVIComparison,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PVINVIComparison'>
            },
            'AccelerationBands': {
                'class': AccelerationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccelerationBands'>
            }
        }),
        ('weights', {
            'PVINVIComparison': 1.0,
            'AccelerationBands': 1.0
        })
    )
