import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HullMovingAverage_ParabolicTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HullMovingAverage und ParabolicTimePrice
    """
    
    params = (
        ('indicators', {
            'HullMovingAverage': {
                'class': HullMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HullMovingAverage'>
            },
            'ParabolicTimePrice': {
                'class': ParabolicTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicTimePrice'>
            }
        }),
        ('weights', {
            'HullMovingAverage': 1.0,
            'ParabolicTimePrice': 1.0
        })
    )
