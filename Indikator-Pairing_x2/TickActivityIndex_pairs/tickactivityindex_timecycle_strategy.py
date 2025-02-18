import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickActivityIndex_TimeCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickActivityIndex und TimeCycle
    """
    
    params = (
        ('indicators', {
            'TickActivityIndex': {
                'class': TickActivityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickActivityIndex'>
            },
            'TimeCycle': {
                'class': TimeCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeCycle'>
            }
        }),
        ('weights', {
            'TickActivityIndex': 1.0,
            'TimeCycle': 1.0
        })
    )
