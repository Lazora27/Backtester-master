import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NVISignals_CyberCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NVISignals und CyberCycleOscillator
    """
    
    params = (
        ('indicators', {
            'NVISignals': {
                'class': NVISignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NVISignals'>
            },
            'CyberCycleOscillator': {
                'class': CyberCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycleOscillator'>
            }
        }),
        ('weights', {
            'NVISignals': 1.0,
            'CyberCycleOscillator': 1.0
        })
    )
