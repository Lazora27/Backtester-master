import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DeltaProfile_SmoothedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DeltaProfile und SmoothedCycle
    """
    
    params = (
        ('indicators', {
            'DeltaProfile': {
                'class': DeltaProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DeltaProfile'>
            },
            'SmoothedCycle': {
                'class': SmoothedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedCycle'>
            }
        }),
        ('weights', {
            'DeltaProfile': 1.0,
            'SmoothedCycle': 1.0
        })
    )
