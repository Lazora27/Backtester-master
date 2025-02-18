import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DynamicMomentumIndex_HullMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DynamicMomentumIndex und HullMovingAverage
    """
    
    params = (
        ('indicators', {
            'DynamicMomentumIndex': {
                'class': DynamicMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DynamicMomentumIndex'>
            },
            'HullMovingAverage': {
                'class': HullMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HullMovingAverage'>
            }
        }),
        ('weights', {
            'DynamicMomentumIndex': 1.0,
            'HullMovingAverage': 1.0
        })
    )
