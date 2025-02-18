import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChandeKrollStop_WeightedMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChandeKrollStop und WeightedMovingAverage
    """
    
    params = (
        ('indicators', {
            'ChandeKrollStop': {
                'class': ChandeKrollStop,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeKrollStop'>
            },
            'WeightedMovingAverage': {
                'class': WeightedMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedMovingAverage'>
            }
        }),
        ('weights', {
            'ChandeKrollStop': 1.0,
            'WeightedMovingAverage': 1.0
        })
    )
