import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ArnaudLegouxMovingAverage_MESAAdaptiveMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ArnaudLegouxMovingAverage und MESAAdaptiveMovingAverage
    """
    
    params = (
        ('indicators', {
            'ArnaudLegouxMovingAverage': {
                'class': ArnaudLegouxMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ArnaudLegouxMovingAverage'>
            },
            'MESAAdaptiveMovingAverage': {
                'class': MESAAdaptiveMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MESAAdaptiveMovingAverage'>
            }
        }),
        ('weights', {
            'ArnaudLegouxMovingAverage': 1.0,
            'MESAAdaptiveMovingAverage': 1.0
        })
    )
