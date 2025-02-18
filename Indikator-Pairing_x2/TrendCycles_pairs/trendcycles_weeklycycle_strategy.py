import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrendCycles_WeeklyCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrendCycles und WeeklyCycle
    """
    
    params = (
        ('indicators', {
            'TrendCycles': {
                'class': TrendCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendCycles'>
            },
            'WeeklyCycle': {
                'class': WeeklyCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeeklyCycle'>
            }
        }),
        ('weights', {
            'TrendCycles': 1.0,
            'WeeklyCycle': 1.0
        })
    )
