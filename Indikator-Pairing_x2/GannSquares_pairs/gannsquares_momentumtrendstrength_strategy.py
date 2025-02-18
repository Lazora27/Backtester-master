import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannSquares_MomentumTrendStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannSquares und MomentumTrendStrength
    """
    
    params = (
        ('indicators', {
            'GannSquares': {
                'class': GannSquares,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquares'>
            },
            'MomentumTrendStrength': {
                'class': MomentumTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumTrendStrength'>
            }
        }),
        ('weights', {
            'GannSquares': 1.0,
            'MomentumTrendStrength': 1.0
        })
    )
