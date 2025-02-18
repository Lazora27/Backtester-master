import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsR_CyberCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsR und CyberCycleOscillator
    """
    
    params = (
        ('indicators', {
            'WilliamsR': {
                'class': WilliamsR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsR1'>
            },
            'CyberCycleOscillator': {
                'class': CyberCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycleOscillator'>
            }
        }),
        ('weights', {
            'WilliamsR': 1.0,
            'CyberCycleOscillator': 1.0
        })
    )
