import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WyckoffAccumulationDistributionIndicator_EaseOfMovement_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WyckoffAccumulationDistributionIndicator und EaseOfMovement
    """
    
    params = (
        ('indicators', {
            'WyckoffAccumulationDistributionIndicator': {
                'class': WyckoffAccumulationDistributionIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WyckoffAccumulationDistributionIndicator'>
            },
            'EaseOfMovement': {
                'class': EaseOfMovement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EaseOfMovement1'>
            }
        }),
        ('weights', {
            'WyckoffAccumulationDistributionIndicator': 1.0,
            'EaseOfMovement': 1.0
        })
    )
