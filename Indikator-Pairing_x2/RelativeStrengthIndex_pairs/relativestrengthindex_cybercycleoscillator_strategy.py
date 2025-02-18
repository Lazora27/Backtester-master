import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RelativeStrengthIndex_CyberCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RelativeStrengthIndex und CyberCycleOscillator
    """
    
    params = (
        ('indicators', {
            'RelativeStrengthIndex': {
                'class': RelativeStrengthIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeStrengthIndex1'>
            },
            'CyberCycleOscillator': {
                'class': CyberCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycleOscillator'>
            }
        }),
        ('weights', {
            'RelativeStrengthIndex': 1.0,
            'CyberCycleOscillator': 1.0
        })
    )
