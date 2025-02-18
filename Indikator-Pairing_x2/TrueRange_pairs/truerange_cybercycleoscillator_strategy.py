import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrueRange_CyberCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrueRange und CyberCycleOscillator
    """
    
    params = (
        ('indicators', {
            'TrueRange': {
                'class': TrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRange1'>
            },
            'CyberCycleOscillator': {
                'class': CyberCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycleOscillator'>
            }
        }),
        ('weights', {
            'TrueRange': 1.0,
            'CyberCycleOscillator': 1.0
        })
    )
