import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ModifiedRSI_MovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ModifiedRSI und MovingAverage
    """
    
    params = (
        ('indicators', {
            'ModifiedRSI': {
                'class': ModifiedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedRSI'>
            },
            'MovingAverage': {
                'class': MovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MovingAverage'>
            }
        }),
        ('weights', {
            'ModifiedRSI': 1.0,
            'MovingAverage': 1.0
        })
    )
