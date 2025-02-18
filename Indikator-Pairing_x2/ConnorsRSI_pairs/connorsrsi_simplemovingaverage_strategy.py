import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ConnorsRSI_SimpleMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ConnorsRSI und SimpleMovingAverage
    """
    
    params = (
        ('indicators', {
            'ConnorsRSI': {
                'class': ConnorsRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ConnorsRSI'>
            },
            'SimpleMovingAverage': {
                'class': SimpleMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SimpleMovingAverage'>
            }
        }),
        ('weights', {
            'ConnorsRSI': 1.0,
            'SimpleMovingAverage': 1.0
        })
    )
