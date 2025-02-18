import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticRSI_WyckoffAccumulationDistributionIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticRSI und WyckoffAccumulationDistributionIndicator
    """
    
    params = (
        ('indicators', {
            'StochasticRSI': {
                'class': StochasticRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticRSI'>
            },
            'WyckoffAccumulationDistributionIndicator': {
                'class': WyckoffAccumulationDistributionIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WyckoffAccumulationDistributionIndicator'>
            }
        }),
        ('weights', {
            'StochasticRSI': 1.0,
            'WyckoffAccumulationDistributionIndicator': 1.0
        })
    )
