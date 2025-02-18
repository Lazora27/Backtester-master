import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PVINVIComparison_TapeReading_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PVINVIComparison und TapeReading
    """
    
    params = (
        ('indicators', {
            'PVINVIComparison': {
                'class': PVINVIComparison,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PVINVIComparison'>
            },
            'TapeReading': {
                'class': TapeReading,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TapeReading'>
            }
        }),
        ('weights', {
            'PVINVIComparison': 1.0,
            'TapeReading': 1.0
        })
    )
