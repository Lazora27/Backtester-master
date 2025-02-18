import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannSquareReversal_MomentumTrendStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannSquareReversal und MomentumTrendStrength
    """
    
    params = (
        ('indicators', {
            'GannSquareReversal': {
                'class': GannSquareReversal,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquareReversal'>
            },
            'MomentumTrendStrength': {
                'class': MomentumTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumTrendStrength'>
            }
        }),
        ('weights', {
            'GannSquareReversal': 1.0,
            'MomentumTrendStrength': 1.0
        })
    )
