import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDPredictor_RainbowMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDPredictor und RainbowMovingAverage
    """
    
    params = (
        ('indicators', {
            'MACDPredictor': {
                'class': MACDPredictor,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDPredictor'>
            },
            'RainbowMovingAverage': {
                'class': RainbowMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RainbowMovingAverage'>
            }
        }),
        ('weights', {
            'MACDPredictor': 1.0,
            'RainbowMovingAverage': 1.0
        })
    )
