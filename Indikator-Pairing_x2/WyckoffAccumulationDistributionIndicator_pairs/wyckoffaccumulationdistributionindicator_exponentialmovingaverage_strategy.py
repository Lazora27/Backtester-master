import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WyckoffAccumulationDistributionIndicator_ExponentialMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WyckoffAccumulationDistributionIndicator und ExponentialMovingAverage
    """
    
    params = (
        ('indicators', {
            'WyckoffAccumulationDistributionIndicator': {
                'class': WyckoffAccumulationDistributionIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WyckoffAccumulationDistributionIndicator'>
            },
            'ExponentialMovingAverage': {
                'class': ExponentialMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExponentialMovingAverage'>
            }
        }),
        ('weights', {
            'WyckoffAccumulationDistributionIndicator': 1.0,
            'ExponentialMovingAverage': 1.0
        })
    )
