import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowIndex_CenterOfGravity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowIndex und CenterOfGravity
    """
    
    params = (
        ('indicators', {
            'HighLowIndex': {
                'class': HighLowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowIndex'>
            },
            'CenterOfGravity': {
                'class': CenterOfGravity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CenterOfGravity'>
            }
        }),
        ('weights', {
            'HighLowIndex': 1.0,
            'CenterOfGravity': 1.0
        })
    )
