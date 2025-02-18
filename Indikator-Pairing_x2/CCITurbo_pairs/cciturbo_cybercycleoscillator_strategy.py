import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CCITurbo_CyberCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CCITurbo und CyberCycleOscillator
    """
    
    params = (
        ('indicators', {
            'CCITurbo': {
                'class': CCITurbo,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CCITurbo'>
            },
            'CyberCycleOscillator': {
                'class': CyberCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycleOscillator'>
            }
        }),
        ('weights', {
            'CCITurbo': 1.0,
            'CyberCycleOscillator': 1.0
        })
    )
