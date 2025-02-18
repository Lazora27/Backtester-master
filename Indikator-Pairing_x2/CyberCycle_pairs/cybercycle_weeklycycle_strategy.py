import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CyberCycle_WeeklyCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CyberCycle und WeeklyCycle
    """
    
    params = (
        ('indicators', {
            'CyberCycle': {
                'class': CyberCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycle'>
            },
            'WeeklyCycle': {
                'class': WeeklyCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeeklyCycle'>
            }
        }),
        ('weights', {
            'CyberCycle': 1.0,
            'WeeklyCycle': 1.0
        })
    )
