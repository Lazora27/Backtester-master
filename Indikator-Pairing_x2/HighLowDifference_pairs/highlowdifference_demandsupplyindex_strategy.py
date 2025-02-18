import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowDifference_DemandSupplyIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowDifference und DemandSupplyIndex
    """
    
    params = (
        ('indicators', {
            'HighLowDifference': {
                'class': HighLowDifference,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowDifference'>
            },
            'DemandSupplyIndex': {
                'class': DemandSupplyIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandSupplyIndex'>
            }
        }),
        ('weights', {
            'HighLowDifference': 1.0,
            'DemandSupplyIndex': 1.0
        })
    )
