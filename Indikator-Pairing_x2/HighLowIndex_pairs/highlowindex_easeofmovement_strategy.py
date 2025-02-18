import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowIndex_EaseOfMovement_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowIndex und EaseOfMovement
    """
    
    params = (
        ('indicators', {
            'HighLowIndex': {
                'class': HighLowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowIndex'>
            },
            'EaseOfMovement': {
                'class': EaseOfMovement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EaseOfMovement1'>
            }
        }),
        ('weights', {
            'HighLowIndex': 1.0,
            'EaseOfMovement': 1.0
        })
    )
