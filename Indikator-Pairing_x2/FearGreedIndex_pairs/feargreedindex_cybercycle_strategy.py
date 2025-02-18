import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FearGreedIndex_CyberCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FearGreedIndex und CyberCycle
    """
    
    params = (
        ('indicators', {
            'FearGreedIndex': {
                'class': FearGreedIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FearGreedIndex'>
            },
            'CyberCycle': {
                'class': CyberCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycle'>
            }
        }),
        ('weights', {
            'FearGreedIndex': 1.0,
            'CyberCycle': 1.0
        })
    )
