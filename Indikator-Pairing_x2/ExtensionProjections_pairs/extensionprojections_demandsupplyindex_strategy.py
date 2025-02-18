import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ExtensionProjections_DemandSupplyIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ExtensionProjections und DemandSupplyIndex
    """
    
    params = (
        ('indicators', {
            'ExtensionProjections': {
                'class': ExtensionProjections,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExtensionProjections'>
            },
            'DemandSupplyIndex': {
                'class': DemandSupplyIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandSupplyIndex'>
            }
        }),
        ('weights', {
            'ExtensionProjections': 1.0,
            'DemandSupplyIndex': 1.0
        })
    )
