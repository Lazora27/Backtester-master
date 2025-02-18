import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDDivergence_HullMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDDivergence und HullMovingAverage
    """
    
    params = (
        ('indicators', {
            'MACDDivergence': {
                'class': MACDDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDDivergence'>
            },
            'HullMovingAverage': {
                'class': HullMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HullMovingAverage'>
            }
        }),
        ('weights', {
            'MACDDivergence': 1.0,
            'HullMovingAverage': 1.0
        })
    )
