import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RelativeVigorIndex_WeightedMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RelativeVigorIndex und WeightedMovingAverage
    """
    
    params = (
        ('indicators', {
            'RelativeVigorIndex': {
                'class': RelativeVigorIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeVigorIndex'>
            },
            'WeightedMovingAverage': {
                'class': WeightedMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedMovingAverage'>
            }
        }),
        ('weights', {
            'RelativeVigorIndex': 1.0,
            'WeightedMovingAverage': 1.0
        })
    )
