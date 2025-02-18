import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MESAAdaptiveMovingAverage_EhlersDecycler_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MESAAdaptiveMovingAverage und EhlersDecycler
    """
    
    params = (
        ('indicators', {
            'MESAAdaptiveMovingAverage': {
                'class': MESAAdaptiveMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MESAAdaptiveMovingAverage'>
            },
            'EhlersDecycler': {
                'class': EhlersDecycler,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersDecycler'>
            }
        }),
        ('weights', {
            'MESAAdaptiveMovingAverage': 1.0,
            'EhlersDecycler': 1.0
        })
    )
