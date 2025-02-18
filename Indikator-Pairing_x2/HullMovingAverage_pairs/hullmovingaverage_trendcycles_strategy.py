import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HullMovingAverage_TrendCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HullMovingAverage und TrendCycles
    """
    
    params = (
        ('indicators', {
            'HullMovingAverage': {
                'class': HullMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HullMovingAverage'>
            },
            'TrendCycles': {
                'class': TrendCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendCycles'>
            }
        }),
        ('weights', {
            'HullMovingAverage': 1.0,
            'TrendCycles': 1.0
        })
    )
