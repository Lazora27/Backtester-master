import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HullMovingAverage_CCITurbo_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HullMovingAverage und CCITurbo
    """
    
    params = (
        ('indicators', {
            'HullMovingAverage': {
                'class': HullMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HullMovingAverage'>
            },
            'CCITurbo': {
                'class': CCITurbo,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CCITurbo'>
            }
        }),
        ('weights', {
            'HullMovingAverage': 1.0,
            'CCITurbo': 1.0
        })
    )
