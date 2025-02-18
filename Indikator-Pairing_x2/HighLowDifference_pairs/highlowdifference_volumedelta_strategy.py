import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowDifference_VolumeDelta_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowDifference und VolumeDelta
    """
    
    params = (
        ('indicators', {
            'HighLowDifference': {
                'class': HighLowDifference,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowDifference'>
            },
            'VolumeDelta': {
                'class': VolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeDelta'>
            }
        }),
        ('weights', {
            'HighLowDifference': 1.0,
            'VolumeDelta': 1.0
        })
    )
