import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CyberCycleOscillator_TimeCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CyberCycleOscillator und TimeCycle
    """
    
    params = (
        ('indicators', {
            'CyberCycleOscillator': {
                'class': CyberCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycleOscillator'>
            },
            'TimeCycle': {
                'class': TimeCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeCycle'>
            }
        }),
        ('weights', {
            'CyberCycleOscillator': 1.0,
            'TimeCycle': 1.0
        })
    )
