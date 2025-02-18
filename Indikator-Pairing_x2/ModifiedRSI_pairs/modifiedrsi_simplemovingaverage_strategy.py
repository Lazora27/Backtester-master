import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ModifiedRSI_SimpleMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ModifiedRSI und SimpleMovingAverage
    """
    
    params = (
        ('indicators', {
            'ModifiedRSI': {
                'class': ModifiedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedRSI'>
            },
            'SimpleMovingAverage': {
                'class': SimpleMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SimpleMovingAverage'>
            }
        }),
        ('weights', {
            'ModifiedRSI': 1.0,
            'SimpleMovingAverage': 1.0
        })
    )
