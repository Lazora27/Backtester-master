import backtrader as bt
from ..base_strategy import FlexibleStrategy

class UlcerIndex_CyberCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von UlcerIndex und CyberCycleOscillator
    """
    
    params = (
        ('indicators', {
            'UlcerIndex': {
                'class': UlcerIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndex'>
            },
            'CyberCycleOscillator': {
                'class': CyberCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycleOscillator'>
            }
        }),
        ('weights', {
            'UlcerIndex': 1.0,
            'CyberCycleOscillator': 1.0
        })
    )
