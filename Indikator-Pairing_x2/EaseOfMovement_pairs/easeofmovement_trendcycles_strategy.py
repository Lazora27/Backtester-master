import backtrader as bt
from ..base_strategy import FlexibleStrategy

class EaseOfMovement_TrendCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von EaseOfMovement und TrendCycles
    """
    
    params = (
        ('indicators', {
            'EaseOfMovement': {
                'class': EaseOfMovement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EaseOfMovement1'>
            },
            'TrendCycles': {
                'class': TrendCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendCycles'>
            }
        }),
        ('weights', {
            'EaseOfMovement': 1.0,
            'TrendCycles': 1.0
        })
    )
