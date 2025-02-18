import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickIndex_CyberCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickIndex und CyberCycle
    """
    
    params = (
        ('indicators', {
            'TickIndex': {
                'class': TickIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickIndex'>
            },
            'CyberCycle': {
                'class': CyberCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycle'>
            }
        }),
        ('weights', {
            'TickIndex': 1.0,
            'CyberCycle': 1.0
        })
    )
