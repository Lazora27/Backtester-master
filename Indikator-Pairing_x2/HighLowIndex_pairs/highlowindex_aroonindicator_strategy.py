import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowIndex_AroonIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowIndex und AroonIndicator
    """
    
    params = (
        ('indicators', {
            'HighLowIndex': {
                'class': HighLowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowIndex'>
            },
            'AroonIndicator': {
                'class': AroonIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AroonIndicator'>
            }
        }),
        ('weights', {
            'HighLowIndex': 1.0,
            'AroonIndicator': 1.0
        })
    )
