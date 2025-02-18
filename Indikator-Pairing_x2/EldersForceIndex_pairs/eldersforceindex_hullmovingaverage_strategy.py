import backtrader as bt
from ..base_strategy import FlexibleStrategy

class EldersForceIndex_HullMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von EldersForceIndex und HullMovingAverage
    """
    
    params = (
        ('indicators', {
            'EldersForceIndex': {
                'class': EldersForceIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EldersForceIndex'>
            },
            'HullMovingAverage': {
                'class': HullMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HullMovingAverage'>
            }
        }),
        ('weights', {
            'EldersForceIndex': 1.0,
            'HullMovingAverage': 1.0
        })
    )
