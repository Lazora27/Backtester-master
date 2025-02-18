import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DemandSupplyIndex_AccumulationDistributionLine_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DemandSupplyIndex und AccumulationDistributionLine
    """
    
    params = (
        ('indicators', {
            'DemandSupplyIndex': {
                'class': DemandSupplyIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandSupplyIndex'>
            },
            'AccumulationDistributionLine': {
                'class': AccumulationDistributionLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccumulationDistributionLine'>
            }
        }),
        ('weights', {
            'DemandSupplyIndex': 1.0,
            'AccumulationDistributionLine': 1.0
        })
    )
