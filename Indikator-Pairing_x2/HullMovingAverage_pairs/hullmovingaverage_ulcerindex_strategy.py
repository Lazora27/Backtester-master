import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HullMovingAverage_UlcerIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HullMovingAverage und UlcerIndex
    """
    
    params = (
        ('indicators', {
            'HullMovingAverage': {
                'class': HullMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HullMovingAverage'>
            },
            'UlcerIndex': {
                'class': UlcerIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndex'>
            }
        }),
        ('weights', {
            'HullMovingAverage': 1.0,
            'UlcerIndex': 1.0
        })
    )
