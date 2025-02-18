import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickIndex_WyckoffAccumulationDistributionIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickIndex und WyckoffAccumulationDistributionIndicator
    """
    
    params = (
        ('indicators', {
            'TickIndex': {
                'class': TickIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickIndex'>
            },
            'WyckoffAccumulationDistributionIndicator': {
                'class': WyckoffAccumulationDistributionIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WyckoffAccumulationDistributionIndicator'>
            }
        }),
        ('weights', {
            'TickIndex': 1.0,
            'WyckoffAccumulationDistributionIndicator': 1.0
        })
    )
