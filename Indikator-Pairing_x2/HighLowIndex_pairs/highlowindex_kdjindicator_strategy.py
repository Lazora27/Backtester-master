import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowIndex_KDJIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowIndex und KDJIndicator
    """
    
    params = (
        ('indicators', {
            'HighLowIndex': {
                'class': HighLowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowIndex'>
            },
            'KDJIndicator': {
                'class': KDJIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KDJIndicator'>
            }
        }),
        ('weights', {
            'HighLowIndex': 1.0,
            'KDJIndicator': 1.0
        })
    )
