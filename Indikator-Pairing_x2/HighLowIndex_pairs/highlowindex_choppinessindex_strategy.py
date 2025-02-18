import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowIndex_ChoppinessIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowIndex und ChoppinessIndex
    """
    
    params = (
        ('indicators', {
            'HighLowIndex': {
                'class': HighLowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowIndex'>
            },
            'ChoppinessIndex': {
                'class': ChoppinessIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChoppinessIndex'>
            }
        }),
        ('weights', {
            'HighLowIndex': 1.0,
            'ChoppinessIndex': 1.0
        })
    )
