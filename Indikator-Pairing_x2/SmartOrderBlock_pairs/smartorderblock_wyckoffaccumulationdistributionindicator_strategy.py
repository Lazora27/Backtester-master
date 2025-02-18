import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmartOrderBlock_WyckoffAccumulationDistributionIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmartOrderBlock und WyckoffAccumulationDistributionIndicator
    """
    
    params = (
        ('indicators', {
            'SmartOrderBlock': {
                'class': SmartOrderBlock,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmartOrderBlock'>
            },
            'WyckoffAccumulationDistributionIndicator': {
                'class': WyckoffAccumulationDistributionIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WyckoffAccumulationDistributionIndicator'>
            }
        }),
        ('weights', {
            'SmartOrderBlock': 1.0,
            'WyckoffAccumulationDistributionIndicator': 1.0
        })
    )
