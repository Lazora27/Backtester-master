import backtrader as bt
from ..base_strategy import FlexibleStrategy

class UltimateOscillator_CyberCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von UltimateOscillator und CyberCycle
    """
    
    params = (
        ('indicators', {
            'UltimateOscillator': {
                'class': UltimateOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UltimateOscillator1'>
            },
            'CyberCycle': {
                'class': CyberCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycle'>
            }
        }),
        ('weights', {
            'UltimateOscillator': 1.0,
            'CyberCycle': 1.0
        })
    )
