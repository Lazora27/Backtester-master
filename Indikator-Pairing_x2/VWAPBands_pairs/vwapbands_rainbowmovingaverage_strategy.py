import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VWAPBands_RainbowMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VWAPBands und RainbowMovingAverage
    """
    
    params = (
        ('indicators', {
            'VWAPBands': {
                'class': VWAPBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPBands'>
            },
            'RainbowMovingAverage': {
                'class': RainbowMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RainbowMovingAverage'>
            }
        }),
        ('weights', {
            'VWAPBands': 1.0,
            'RainbowMovingAverage': 1.0
        })
    )
