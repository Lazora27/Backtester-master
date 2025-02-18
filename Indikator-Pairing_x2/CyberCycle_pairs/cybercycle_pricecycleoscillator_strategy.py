import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CyberCycle_PriceCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CyberCycle und PriceCycleOscillator
    """
    
    params = (
        ('indicators', {
            'CyberCycle': {
                'class': CyberCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycle'>
            },
            'PriceCycleOscillator': {
                'class': PriceCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceCycleOscillator'>
            }
        }),
        ('weights', {
            'CyberCycle': 1.0,
            'PriceCycleOscillator': 1.0
        })
    )
