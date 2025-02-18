import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HullMovingAverage_BarStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HullMovingAverage und BarStrength
    """
    
    params = (
        ('indicators', {
            'HullMovingAverage': {
                'class': HullMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HullMovingAverage'>
            },
            'BarStrength': {
                'class': BarStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BarStrength'>
            }
        }),
        ('weights', {
            'HullMovingAverage': 1.0,
            'BarStrength': 1.0
        })
    )
