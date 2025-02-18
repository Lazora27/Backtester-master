import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VWAPDeviationBands_WeightedMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VWAPDeviationBands und WeightedMovingAverage
    """
    
    params = (
        ('indicators', {
            'VWAPDeviationBands': {
                'class': VWAPDeviationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPDeviationBands'>
            },
            'WeightedMovingAverage': {
                'class': WeightedMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedMovingAverage'>
            }
        }),
        ('weights', {
            'VWAPDeviationBands': 1.0,
            'WeightedMovingAverage': 1.0
        })
    )
