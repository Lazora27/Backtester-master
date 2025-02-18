import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HullMovingAverage_DemandIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HullMovingAverage und DemandIndex
    """
    
    params = (
        ('indicators', {
            'HullMovingAverage': {
                'class': HullMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HullMovingAverage'>
            },
            'DemandIndex': {
                'class': DemandIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandIndex'>
            }
        }),
        ('weights', {
            'HullMovingAverage': 1.0,
            'DemandIndex': 1.0
        })
    )
