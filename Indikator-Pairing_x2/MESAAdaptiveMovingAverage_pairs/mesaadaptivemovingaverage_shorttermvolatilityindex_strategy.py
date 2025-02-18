import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MESAAdaptiveMovingAverage_ShortTermVolatilityIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MESAAdaptiveMovingAverage und ShortTermVolatilityIndex
    """
    
    params = (
        ('indicators', {
            'MESAAdaptiveMovingAverage': {
                'class': MESAAdaptiveMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MESAAdaptiveMovingAverage'>
            },
            'ShortTermVolatilityIndex': {
                'class': ShortTermVolatilityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ShortTermVolatilityIndex'>
            }
        }),
        ('weights', {
            'MESAAdaptiveMovingAverage': 1.0,
            'ShortTermVolatilityIndex': 1.0
        })
    )
