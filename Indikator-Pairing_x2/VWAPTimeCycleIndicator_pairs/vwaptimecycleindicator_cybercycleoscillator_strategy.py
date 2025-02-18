import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VWAPTimeCycleIndicator_CyberCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VWAPTimeCycleIndicator und CyberCycleOscillator
    """
    
    params = (
        ('indicators', {
            'VWAPTimeCycleIndicator': {
                'class': VWAPTimeCycleIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPTimeCycleIndicator'>
            },
            'CyberCycleOscillator': {
                'class': CyberCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycleOscillator'>
            }
        }),
        ('weights', {
            'VWAPTimeCycleIndicator': 1.0,
            'CyberCycleOscillator': 1.0
        })
    )
