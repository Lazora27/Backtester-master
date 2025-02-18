import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowDifference_GannAngles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowDifference und GannAngles
    """
    
    params = (
        ('indicators', {
            'HighLowDifference': {
                'class': HighLowDifference,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowDifference'>
            },
            'GannAngles': {
                'class': GannAngles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannAngles1'>
            }
        }),
        ('weights', {
            'HighLowDifference': 1.0,
            'GannAngles': 1.0
        })
    )
