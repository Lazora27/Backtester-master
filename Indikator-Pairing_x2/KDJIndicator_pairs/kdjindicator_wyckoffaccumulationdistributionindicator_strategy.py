import backtrader as bt
from ..base_strategy import FlexibleStrategy

class KDJIndicator_WyckoffAccumulationDistributionIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von KDJIndicator und WyckoffAccumulationDistributionIndicator
    """
    
    params = (
        ('indicators', {
            'KDJIndicator': {
                'class': KDJIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KDJIndicator'>
            },
            'WyckoffAccumulationDistributionIndicator': {
                'class': WyckoffAccumulationDistributionIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WyckoffAccumulationDistributionIndicator'>
            }
        }),
        ('weights', {
            'KDJIndicator': 1.0,
            'WyckoffAccumulationDistributionIndicator': 1.0
        })
    )
