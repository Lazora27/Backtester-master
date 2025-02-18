import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MomentumIndicator_HullMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MomentumIndicator und HullMovingAverage
    """
    
    params = (
        ('indicators', {
            'MomentumIndicator': {
                'class': MomentumIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumIndicator'>
            },
            'HullMovingAverage': {
                'class': HullMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HullMovingAverage'>
            }
        }),
        ('weights', {
            'MomentumIndicator': 1.0,
            'HullMovingAverage': 1.0
        })
    )
