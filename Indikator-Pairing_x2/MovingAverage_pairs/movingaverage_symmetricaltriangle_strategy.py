import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MovingAverage_SymmetricalTriangle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MovingAverage und SymmetricalTriangle
    """
    
    params = (
        ('indicators', {
            'MovingAverage': {
                'class': MovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MovingAverage'>
            },
            'SymmetricalTriangle': {
                'class': SymmetricalTriangle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SymmetricalTriangle'>
            }
        }),
        ('weights', {
            'MovingAverage': 1.0,
            'SymmetricalTriangle': 1.0
        })
    )
