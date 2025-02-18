import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AccumulationDistributionLine_DemandIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AccumulationDistributionLine und DemandIndex
    """
    
    params = (
        ('indicators', {
            'AccumulationDistributionLine': {
                'class': AccumulationDistributionLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccumulationDistributionLine'>
            },
            'DemandIndex': {
                'class': DemandIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandIndex'>
            }
        }),
        ('weights', {
            'AccumulationDistributionLine': 1.0,
            'DemandIndex': 1.0
        })
    )
