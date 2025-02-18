import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AroonIndicator_CyberCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AroonIndicator und CyberCycleOscillator
    """
    
    params = (
        ('indicators', {
            'AroonIndicator': {
                'class': AroonIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AroonIndicator'>
            },
            'CyberCycleOscillator': {
                'class': CyberCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycleOscillator'>
            }
        }),
        ('weights', {
            'AroonIndicator': 1.0,
            'CyberCycleOscillator': 1.0
        })
    )
