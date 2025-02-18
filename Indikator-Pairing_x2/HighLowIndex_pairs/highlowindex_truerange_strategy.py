import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowIndex_TrueRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowIndex und TrueRange
    """
    
    params = (
        ('indicators', {
            'HighLowIndex': {
                'class': HighLowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowIndex'>
            },
            'TrueRange': {
                'class': TrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRange1'>
            }
        }),
        ('weights', {
            'HighLowIndex': 1.0,
            'TrueRange': 1.0
        })
    )
