import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FisherTransform_DemandSupplyIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FisherTransform und DemandSupplyIndex
    """
    
    params = (
        ('indicators', {
            'FisherTransform': {
                'class': FisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherTransform'>
            },
            'DemandSupplyIndex': {
                'class': DemandSupplyIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandSupplyIndex'>
            }
        }),
        ('weights', {
            'FisherTransform': 1.0,
            'DemandSupplyIndex': 1.0
        })
    )
