import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickIndex_TimeCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickIndex und TimeCycle
    """
    
    params = (
        ('indicators', {
            'TickIndex': {
                'class': TickIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickIndex'>
            },
            'TimeCycle': {
                'class': TimeCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeCycle'>
            }
        }),
        ('weights', {
            'TickIndex': 1.0,
            'TimeCycle': 1.0
        })
    )
