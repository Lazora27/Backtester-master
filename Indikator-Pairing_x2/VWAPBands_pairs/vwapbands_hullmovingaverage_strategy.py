import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VWAPBands_HullMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VWAPBands und HullMovingAverage
    """
    
    params = (
        ('indicators', {
            'VWAPBands': {
                'class': VWAPBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPBands'>
            },
            'HullMovingAverage': {
                'class': HullMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HullMovingAverage'>
            }
        }),
        ('weights', {
            'VWAPBands': 1.0,
            'HullMovingAverage': 1.0
        })
    )
