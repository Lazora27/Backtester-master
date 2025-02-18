import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RainbowMovingAverage_SymmetricalTriangle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RainbowMovingAverage und SymmetricalTriangle
    """
    
    params = (
        ('indicators', {
            'RainbowMovingAverage': {
                'class': RainbowMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RainbowMovingAverage'>
            },
            'SymmetricalTriangle': {
                'class': SymmetricalTriangle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SymmetricalTriangle'>
            }
        }),
        ('weights', {
            'RainbowMovingAverage': 1.0,
            'SymmetricalTriangle': 1.0
        })
    )
