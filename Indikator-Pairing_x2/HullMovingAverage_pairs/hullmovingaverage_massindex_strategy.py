import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HullMovingAverage_MassIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HullMovingAverage und MassIndex
    """
    
    params = (
        ('indicators', {
            'HullMovingAverage': {
                'class': HullMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HullMovingAverage'>
            },
            'MassIndex': {
                'class': MassIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MassIndex'>
            }
        }),
        ('weights', {
            'HullMovingAverage': 1.0,
            'MassIndex': 1.0
        })
    )
