import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WyckoffAccumulationDistributionIndicator_SuperTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WyckoffAccumulationDistributionIndicator und SuperTrend
    """
    
    params = (
        ('indicators', {
            'WyckoffAccumulationDistributionIndicator': {
                'class': WyckoffAccumulationDistributionIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WyckoffAccumulationDistributionIndicator'>
            },
            'SuperTrend': {
                'class': SuperTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperTrend'>
            }
        }),
        ('weights', {
            'WyckoffAccumulationDistributionIndicator': 1.0,
            'SuperTrend': 1.0
        })
    )
