import backtrader as bt
from ..base_strategy import FlexibleStrategy

class Fisher_MomentumTrendStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von Fisher und MomentumTrendStrength
    """
    
    params = (
        ('indicators', {
            'Fisher': {
                'class': Fisher,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_Fisher'>
            },
            'MomentumTrendStrength': {
                'class': MomentumTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumTrendStrength'>
            }
        }),
        ('weights', {
            'Fisher': 1.0,
            'MomentumTrendStrength': 1.0
        })
    )
