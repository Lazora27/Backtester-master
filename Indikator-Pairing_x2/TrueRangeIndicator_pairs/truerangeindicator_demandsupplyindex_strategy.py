import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrueRangeIndicator_DemandSupplyIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrueRangeIndicator und DemandSupplyIndex
    """
    
    params = (
        ('indicators', {
            'TrueRangeIndicator': {
                'class': TrueRangeIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRangeIndicator'>
            },
            'DemandSupplyIndex': {
                'class': DemandSupplyIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandSupplyIndex'>
            }
        }),
        ('weights', {
            'TrueRangeIndicator': 1.0,
            'DemandSupplyIndex': 1.0
        })
    )
