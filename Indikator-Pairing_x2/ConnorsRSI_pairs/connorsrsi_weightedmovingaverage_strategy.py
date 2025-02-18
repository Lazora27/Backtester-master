import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ConnorsRSI_WeightedMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ConnorsRSI und WeightedMovingAverage
    """
    
    params = (
        ('indicators', {
            'ConnorsRSI': {
                'class': ConnorsRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ConnorsRSI'>
            },
            'WeightedMovingAverage': {
                'class': WeightedMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedMovingAverage'>
            }
        }),
        ('weights', {
            'ConnorsRSI': 1.0,
            'WeightedMovingAverage': 1.0
        })
    )
