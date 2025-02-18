import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoSupportResistance_DemandSupplyIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoSupportResistance und DemandSupplyIndex
    """
    
    params = (
        ('indicators', {
            'AutoSupportResistance': {
                'class': AutoSupportResistance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoSupportResistance'>
            },
            'DemandSupplyIndex': {
                'class': DemandSupplyIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandSupplyIndex'>
            }
        }),
        ('weights', {
            'AutoSupportResistance': 1.0,
            'DemandSupplyIndex': 1.0
        })
    )
