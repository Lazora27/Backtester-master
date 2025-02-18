import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AndrewsPitchfork_WyckoffAccumulationDistributionIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AndrewsPitchfork und WyckoffAccumulationDistributionIndicator
    """
    
    params = (
        ('indicators', {
            'AndrewsPitchfork': {
                'class': AndrewsPitchfork,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AndrewsPitchfork'>
            },
            'WyckoffAccumulationDistributionIndicator': {
                'class': WyckoffAccumulationDistributionIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WyckoffAccumulationDistributionIndicator'>
            }
        }),
        ('weights', {
            'AndrewsPitchfork': 1.0,
            'WyckoffAccumulationDistributionIndicator': 1.0
        })
    )
