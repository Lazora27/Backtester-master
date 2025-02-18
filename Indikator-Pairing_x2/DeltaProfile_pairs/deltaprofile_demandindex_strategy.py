import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DeltaProfile_DemandIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DeltaProfile und DemandIndex
    """
    
    params = (
        ('indicators', {
            'DeltaProfile': {
                'class': DeltaProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DeltaProfile'>
            },
            'DemandIndex': {
                'class': DemandIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandIndex'>
            }
        }),
        ('weights', {
            'DeltaProfile': 1.0,
            'DemandIndex': 1.0
        })
    )
