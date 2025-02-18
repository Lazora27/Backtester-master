import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ArmsIndex_CyberCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ArmsIndex und CyberCycle
    """
    
    params = (
        ('indicators', {
            'ArmsIndex': {
                'class': ArmsIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ArmsIndex'>
            },
            'CyberCycle': {
                'class': CyberCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycle'>
            }
        }),
        ('weights', {
            'ArmsIndex': 1.0,
            'CyberCycle': 1.0
        })
    )
