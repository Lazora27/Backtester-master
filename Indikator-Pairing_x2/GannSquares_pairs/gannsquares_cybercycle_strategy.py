import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannSquares_CyberCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannSquares und CyberCycle
    """
    
    params = (
        ('indicators', {
            'GannSquares': {
                'class': GannSquares,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquares'>
            },
            'CyberCycle': {
                'class': CyberCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycle'>
            }
        }),
        ('weights', {
            'GannSquares': 1.0,
            'CyberCycle': 1.0
        })
    )
