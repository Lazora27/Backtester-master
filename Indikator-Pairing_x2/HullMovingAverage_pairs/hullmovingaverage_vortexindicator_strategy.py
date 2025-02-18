import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HullMovingAverage_VortexIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HullMovingAverage und VortexIndicator
    """
    
    params = (
        ('indicators', {
            'HullMovingAverage': {
                'class': HullMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HullMovingAverage'>
            },
            'VortexIndicator': {
                'class': VortexIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VortexIndicator'>
            }
        }),
        ('weights', {
            'HullMovingAverage': 1.0,
            'VortexIndicator': 1.0
        })
    )
