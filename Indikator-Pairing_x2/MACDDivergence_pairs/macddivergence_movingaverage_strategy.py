import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDDivergence_MovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDDivergence und MovingAverage
    """
    
    params = (
        ('indicators', {
            'MACDDivergence': {
                'class': MACDDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDDivergence'>
            },
            'MovingAverage': {
                'class': MovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MovingAverage'>
            }
        }),
        ('weights', {
            'MACDDivergence': 1.0,
            'MovingAverage': 1.0
        })
    )
