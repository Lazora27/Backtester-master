import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VWAPBands_SimpleMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VWAPBands und SimpleMovingAverage
    """
    
    params = (
        ('indicators', {
            'VWAPBands': {
                'class': VWAPBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPBands'>
            },
            'SimpleMovingAverage': {
                'class': SimpleMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SimpleMovingAverage'>
            }
        }),
        ('weights', {
            'VWAPBands': 1.0,
            'SimpleMovingAverage': 1.0
        })
    )
