import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ConnorsRSI_ExponentialMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ConnorsRSI und ExponentialMovingAverage
    """
    
    params = (
        ('indicators', {
            'ConnorsRSI': {
                'class': ConnorsRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ConnorsRSI'>
            },
            'ExponentialMovingAverage': {
                'class': ExponentialMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExponentialMovingAverage'>
            }
        }),
        ('weights', {
            'ConnorsRSI': 1.0,
            'ExponentialMovingAverage': 1.0
        })
    )
