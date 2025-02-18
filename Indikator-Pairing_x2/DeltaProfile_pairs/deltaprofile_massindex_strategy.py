import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DeltaProfile_MassIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DeltaProfile und MassIndex
    """
    
    params = (
        ('indicators', {
            'DeltaProfile': {
                'class': DeltaProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DeltaProfile'>
            },
            'MassIndex': {
                'class': MassIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MassIndex'>
            }
        }),
        ('weights', {
            'DeltaProfile': 1.0,
            'MassIndex': 1.0
        })
    )
