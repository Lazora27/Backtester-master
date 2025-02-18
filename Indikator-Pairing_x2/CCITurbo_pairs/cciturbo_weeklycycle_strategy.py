import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CCITurbo_WeeklyCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CCITurbo und WeeklyCycle
    """
    
    params = (
        ('indicators', {
            'CCITurbo': {
                'class': CCITurbo,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CCITurbo'>
            },
            'WeeklyCycle': {
                'class': WeeklyCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeeklyCycle'>
            }
        }),
        ('weights', {
            'CCITurbo': 1.0,
            'WeeklyCycle': 1.0
        })
    )
