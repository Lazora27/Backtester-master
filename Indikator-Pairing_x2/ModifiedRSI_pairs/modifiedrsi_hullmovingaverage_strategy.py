import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ModifiedRSI_HullMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ModifiedRSI und HullMovingAverage
    """
    
    params = (
        ('indicators', {
            'ModifiedRSI': {
                'class': ModifiedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedRSI'>
            },
            'HullMovingAverage': {
                'class': HullMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HullMovingAverage'>
            }
        }),
        ('weights', {
            'ModifiedRSI': 1.0,
            'HullMovingAverage': 1.0
        })
    )
