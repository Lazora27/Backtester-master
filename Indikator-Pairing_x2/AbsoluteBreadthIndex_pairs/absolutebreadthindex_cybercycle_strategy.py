import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AbsoluteBreadthIndex_CyberCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AbsoluteBreadthIndex und CyberCycle
    """
    
    params = (
        ('indicators', {
            'AbsoluteBreadthIndex': {
                'class': AbsoluteBreadthIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AbsoluteBreadthIndex'>
            },
            'CyberCycle': {
                'class': CyberCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycle'>
            }
        }),
        ('weights', {
            'AbsoluteBreadthIndex': 1.0,
            'CyberCycle': 1.0
        })
    )
