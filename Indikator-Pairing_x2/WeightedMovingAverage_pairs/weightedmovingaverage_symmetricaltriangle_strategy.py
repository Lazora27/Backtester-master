import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WeightedMovingAverage_SymmetricalTriangle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WeightedMovingAverage und SymmetricalTriangle
    """
    
    params = (
        ('indicators', {
            'WeightedMovingAverage': {
                'class': WeightedMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedMovingAverage'>
            },
            'SymmetricalTriangle': {
                'class': SymmetricalTriangle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SymmetricalTriangle'>
            }
        }),
        ('weights', {
            'WeightedMovingAverage': 1.0,
            'SymmetricalTriangle': 1.0
        })
    )
