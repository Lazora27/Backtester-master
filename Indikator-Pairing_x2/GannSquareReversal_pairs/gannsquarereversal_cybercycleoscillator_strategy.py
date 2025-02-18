import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannSquareReversal_CyberCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannSquareReversal und CyberCycleOscillator
    """
    
    params = (
        ('indicators', {
            'GannSquareReversal': {
                'class': GannSquareReversal,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquareReversal'>
            },
            'CyberCycleOscillator': {
                'class': CyberCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycleOscillator'>
            }
        }),
        ('weights', {
            'GannSquareReversal': 1.0,
            'CyberCycleOscillator': 1.0
        })
    )
