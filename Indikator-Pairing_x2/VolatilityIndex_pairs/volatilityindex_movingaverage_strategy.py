import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolatilityIndex_MovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolatilityIndex und MovingAverage
    """
    
    params = (
        ('indicators', {
            'VolatilityIndex': {
                'class': VolatilityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolatilityIndex'>
            },
            'MovingAverage': {
                'class': MovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MovingAverage'>
            }
        }),
        ('weights', {
            'VolatilityIndex': 1.0,
            'MovingAverage': 1.0
        })
    )
