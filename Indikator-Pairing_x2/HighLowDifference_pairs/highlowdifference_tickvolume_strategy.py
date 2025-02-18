import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowDifference_TickVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowDifference und TickVolume
    """
    
    params = (
        ('indicators', {
            'HighLowDifference': {
                'class': HighLowDifference,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowDifference'>
            },
            'TickVolume': {
                'class': TickVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickVolume'>
            }
        }),
        ('weights', {
            'HighLowDifference': 1.0,
            'TickVolume': 1.0
        })
    )
