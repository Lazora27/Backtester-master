import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannSquareReversal_CyberCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannSquareReversal und CyberCycle
    """
    
    params = (
        ('indicators', {
            'GannSquareReversal': {
                'class': GannSquareReversal,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquareReversal'>
            },
            'CyberCycle': {
                'class': CyberCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycle'>
            }
        }),
        ('weights', {
            'GannSquareReversal': 1.0,
            'CyberCycle': 1.0
        })
    )
