import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannAngles_CyberCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannAngles und CyberCycleOscillator
    """
    
    params = (
        ('indicators', {
            'GannAngles': {
                'class': GannAngles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannAngles1'>
            },
            'CyberCycleOscillator': {
                'class': CyberCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycleOscillator'>
            }
        }),
        ('weights', {
            'GannAngles': 1.0,
            'CyberCycleOscillator': 1.0
        })
    )
