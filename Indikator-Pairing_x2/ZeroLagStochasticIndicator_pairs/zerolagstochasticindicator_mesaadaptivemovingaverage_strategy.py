import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ZeroLagStochasticIndicator_MESAAdaptiveMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ZeroLagStochasticIndicator und MESAAdaptiveMovingAverage
    """
    
    params = (
        ('indicators', {
            'ZeroLagStochasticIndicator': {
                'class': ZeroLagStochasticIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ZeroLagStochasticIndicator'>
            },
            'MESAAdaptiveMovingAverage': {
                'class': MESAAdaptiveMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MESAAdaptiveMovingAverage'>
            }
        }),
        ('weights', {
            'ZeroLagStochasticIndicator': 1.0,
            'MESAAdaptiveMovingAverage': 1.0
        })
    )
