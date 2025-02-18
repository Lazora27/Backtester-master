import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DeltaProfile_DemandSupplyIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DeltaProfile und DemandSupplyIndex
    """
    
    params = (
        ('indicators', {
            'DeltaProfile': {
                'class': DeltaProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DeltaProfile'>
            },
            'DemandSupplyIndex': {
                'class': DemandSupplyIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandSupplyIndex'>
            }
        }),
        ('weights', {
            'DeltaProfile': 1.0,
            'DemandSupplyIndex': 1.0
        })
    )
