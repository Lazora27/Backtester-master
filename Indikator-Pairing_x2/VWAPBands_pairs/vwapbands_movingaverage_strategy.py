import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VWAPBands_MovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VWAPBands und MovingAverage
    """
    
    params = (
        ('indicators', {
            'VWAPBands': {
                'class': VWAPBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPBands'>
            },
            'MovingAverage': {
                'class': MovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MovingAverage'>
            }
        }),
        ('weights', {
            'VWAPBands': 1.0,
            'MovingAverage': 1.0
        })
    )
