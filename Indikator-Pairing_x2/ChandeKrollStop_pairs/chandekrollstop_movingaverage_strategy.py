import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChandeKrollStop_MovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChandeKrollStop und MovingAverage
    """
    
    params = (
        ('indicators', {
            'ChandeKrollStop': {
                'class': ChandeKrollStop,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeKrollStop'>
            },
            'MovingAverage': {
                'class': MovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MovingAverage'>
            }
        }),
        ('weights', {
            'ChandeKrollStop': 1.0,
            'MovingAverage': 1.0
        })
    )
