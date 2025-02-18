import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DemandSupplyIndex_EhlersFisherTransform_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DemandSupplyIndex und EhlersFisherTransform
    """
    
    params = (
        ('indicators', {
            'DemandSupplyIndex': {
                'class': DemandSupplyIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandSupplyIndex'>
            },
            'EhlersFisherTransform': {
                'class': EhlersFisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersFisherTransform'>
            }
        }),
        ('weights', {
            'DemandSupplyIndex': 1.0,
            'EhlersFisherTransform': 1.0
        })
    )
