import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDDivergence_SimpleMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDDivergence und SimpleMovingAverage
    """
    
    params = (
        ('indicators', {
            'MACDDivergence': {
                'class': MACDDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDDivergence'>
            },
            'SimpleMovingAverage': {
                'class': SimpleMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SimpleMovingAverage'>
            }
        }),
        ('weights', {
            'MACDDivergence': 1.0,
            'SimpleMovingAverage': 1.0
        })
    )
