import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VWAPDeviationBands_RainbowMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VWAPDeviationBands und RainbowMovingAverage
    """
    
    params = (
        ('indicators', {
            'VWAPDeviationBands': {
                'class': VWAPDeviationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPDeviationBands'>
            },
            'RainbowMovingAverage': {
                'class': RainbowMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RainbowMovingAverage'>
            }
        }),
        ('weights', {
            'VWAPDeviationBands': 1.0,
            'RainbowMovingAverage': 1.0
        })
    )
