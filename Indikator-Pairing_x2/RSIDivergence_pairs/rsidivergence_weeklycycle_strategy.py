import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RSIDivergence_WeeklyCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RSIDivergence und WeeklyCycle
    """
    
    params = (
        ('indicators', {
            'RSIDivergence': {
                'class': RSIDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RSIDivergence'>
            },
            'WeeklyCycle': {
                'class': WeeklyCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeeklyCycle'>
            }
        }),
        ('weights', {
            'RSIDivergence': 1.0,
            'WeeklyCycle': 1.0
        })
    )
