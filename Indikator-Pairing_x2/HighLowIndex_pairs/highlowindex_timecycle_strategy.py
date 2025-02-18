import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowIndex_TimeCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowIndex und TimeCycle
    """
    
    params = (
        ('indicators', {
            'HighLowIndex': {
                'class': HighLowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowIndex'>
            },
            'TimeCycle': {
                'class': TimeCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeCycle'>
            }
        }),
        ('weights', {
            'HighLowIndex': 1.0,
            'TimeCycle': 1.0
        })
    )
