import backtrader as bt
from ..base_strategy import FlexibleStrategy

class IchimokuCloud_DemandSupplyIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von IchimokuCloud und DemandSupplyIndex
    """
    
    params = (
        ('indicators', {
            'IchimokuCloud': {
                'class': IchimokuCloud,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IchimokuCloud'>
            },
            'DemandSupplyIndex': {
                'class': DemandSupplyIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandSupplyIndex'>
            }
        }),
        ('weights', {
            'IchimokuCloud': 1.0,
            'DemandSupplyIndex': 1.0
        })
    )
