import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdvancedCandlePattern_WeeklyCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdvancedCandlePattern und WeeklyCycle
    """
    
    params = (
        ('indicators', {
            'AdvancedCandlePattern': {
                'class': AdvancedCandlePattern,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdvancedCandlePattern'>
            },
            'WeeklyCycle': {
                'class': WeeklyCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeeklyCycle'>
            }
        }),
        ('weights', {
            'AdvancedCandlePattern': 1.0,
            'WeeklyCycle': 1.0
        })
    )
