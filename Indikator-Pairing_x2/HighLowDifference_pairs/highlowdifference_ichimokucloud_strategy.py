import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowDifference_IchimokuCloud_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowDifference und IchimokuCloud
    """
    
    params = (
        ('indicators', {
            'HighLowDifference': {
                'class': HighLowDifference,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowDifference'>
            },
            'IchimokuCloud': {
                'class': IchimokuCloud,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IchimokuCloud'>
            }
        }),
        ('weights', {
            'HighLowDifference': 1.0,
            'IchimokuCloud': 1.0
        })
    )
