import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannSquares_CyberCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannSquares und CyberCycleOscillator
    """
    
    params = (
        ('indicators', {
            'GannSquares': {
                'class': GannSquares,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquares'>
            },
            'CyberCycleOscillator': {
                'class': CyberCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycleOscillator'>
            }
        }),
        ('weights', {
            'GannSquares': 1.0,
            'CyberCycleOscillator': 1.0
        })
    )
