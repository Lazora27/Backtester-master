import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FearGreedIndex_CyberCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FearGreedIndex und CyberCycleOscillator
    """
    
    params = (
        ('indicators', {
            'FearGreedIndex': {
                'class': FearGreedIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FearGreedIndex'>
            },
            'CyberCycleOscillator': {
                'class': CyberCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycleOscillator'>
            }
        }),
        ('weights', {
            'FearGreedIndex': 1.0,
            'CyberCycleOscillator': 1.0
        })
    )
