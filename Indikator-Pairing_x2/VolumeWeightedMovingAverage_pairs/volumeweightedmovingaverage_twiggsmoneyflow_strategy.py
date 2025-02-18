import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeWeightedMovingAverage_TwiggsMoneyFlow_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeWeightedMovingAverage und TwiggsMoneyFlow
    """
    
    params = (
        ('indicators', {
            'VolumeWeightedMovingAverage': {
                'class': VolumeWeightedMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeWeightedMovingAverage'>
            },
            'TwiggsMoneyFlow': {
                'class': TwiggsMoneyFlow,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TwiggsMoneyFlow'>
            }
        }),
        ('weights', {
            'VolumeWeightedMovingAverage': 1.0,
            'TwiggsMoneyFlow': 1.0
        })
    )
