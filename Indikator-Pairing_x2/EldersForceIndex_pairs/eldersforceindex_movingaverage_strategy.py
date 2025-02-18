import backtrader as bt
from ..base_strategy import FlexibleStrategy

class EldersForceIndex_MovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von EldersForceIndex und MovingAverage
    """
    
    params = (
        ('indicators', {
            'EldersForceIndex': {
                'class': EldersForceIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EldersForceIndex'>
            },
            'MovingAverage': {
                'class': MovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MovingAverage'>
            }
        }),
        ('weights', {
            'EldersForceIndex': 1.0,
            'MovingAverage': 1.0
        })
    )
