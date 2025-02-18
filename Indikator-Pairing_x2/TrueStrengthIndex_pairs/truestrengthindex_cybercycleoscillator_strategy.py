import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrueStrengthIndex_CyberCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrueStrengthIndex und CyberCycleOscillator
    """
    
    params = (
        ('indicators', {
            'TrueStrengthIndex': {
                'class': TrueStrengthIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueStrengthIndex'>
            },
            'CyberCycleOscillator': {
                'class': CyberCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycleOscillator'>
            }
        }),
        ('weights', {
            'TrueStrengthIndex': 1.0,
            'CyberCycleOscillator': 1.0
        })
    )
