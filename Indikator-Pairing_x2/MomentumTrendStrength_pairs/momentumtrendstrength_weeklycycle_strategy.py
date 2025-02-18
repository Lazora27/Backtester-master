import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MomentumTrendStrength_WeeklyCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MomentumTrendStrength und WeeklyCycle
    """
    
    params = (
        ('indicators', {
            'MomentumTrendStrength': {
                'class': MomentumTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumTrendStrength'>
            },
            'WeeklyCycle': {
                'class': WeeklyCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeeklyCycle'>
            }
        }),
        ('weights', {
            'MomentumTrendStrength': 1.0,
            'WeeklyCycle': 1.0
        })
    )
