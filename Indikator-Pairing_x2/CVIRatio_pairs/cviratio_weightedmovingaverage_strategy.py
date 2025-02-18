import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CVIRatio_WeightedMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CVIRatio und WeightedMovingAverage
    """
    
    params = (
        ('indicators', {
            'CVIRatio': {
                'class': CVIRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CVIRatio'>
            },
            'WeightedMovingAverage': {
                'class': WeightedMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedMovingAverage'>
            }
        }),
        ('weights', {
            'CVIRatio': 1.0,
            'WeightedMovingAverage': 1.0
        })
    )
