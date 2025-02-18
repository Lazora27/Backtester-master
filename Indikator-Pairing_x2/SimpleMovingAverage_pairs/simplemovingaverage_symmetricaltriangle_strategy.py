import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SimpleMovingAverage_SymmetricalTriangle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SimpleMovingAverage und SymmetricalTriangle
    """
    
    params = (
        ('indicators', {
            'SimpleMovingAverage': {
                'class': SimpleMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SimpleMovingAverage'>
            },
            'SymmetricalTriangle': {
                'class': SymmetricalTriangle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SymmetricalTriangle'>
            }
        }),
        ('weights', {
            'SimpleMovingAverage': 1.0,
            'SymmetricalTriangle': 1.0
        })
    )
