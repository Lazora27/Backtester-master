import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDPredictor_MovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDPredictor und MovingAverage
    """
    
    params = (
        ('indicators', {
            'MACDPredictor': {
                'class': MACDPredictor,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDPredictor'>
            },
            'MovingAverage': {
                'class': MovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MovingAverage'>
            }
        }),
        ('weights', {
            'MACDPredictor': 1.0,
            'MovingAverage': 1.0
        })
    )
