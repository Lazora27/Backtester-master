import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickActivityIndex_CyberCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickActivityIndex und CyberCycle
    """
    
    params = (
        ('indicators', {
            'TickActivityIndex': {
                'class': TickActivityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickActivityIndex'>
            },
            'CyberCycle': {
                'class': CyberCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycle'>
            }
        }),
        ('weights', {
            'TickActivityIndex': 1.0,
            'CyberCycle': 1.0
        })
    )
