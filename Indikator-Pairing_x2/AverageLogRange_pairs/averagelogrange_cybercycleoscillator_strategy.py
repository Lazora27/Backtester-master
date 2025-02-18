import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AverageLogRange_CyberCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AverageLogRange und CyberCycleOscillator
    """
    
    params = (
        ('indicators', {
            'AverageLogRange': {
                'class': AverageLogRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageLogRange'>
            },
            'CyberCycleOscillator': {
                'class': CyberCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycleOscillator'>
            }
        }),
        ('weights', {
            'AverageLogRange': 1.0,
            'CyberCycleOscillator': 1.0
        })
    )
