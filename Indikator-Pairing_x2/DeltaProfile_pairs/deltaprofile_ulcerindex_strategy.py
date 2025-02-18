import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DeltaProfile_UlcerIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DeltaProfile und UlcerIndex
    """
    
    params = (
        ('indicators', {
            'DeltaProfile': {
                'class': DeltaProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DeltaProfile'>
            },
            'UlcerIndex': {
                'class': UlcerIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndex'>
            }
        }),
        ('weights', {
            'DeltaProfile': 1.0,
            'UlcerIndex': 1.0
        })
    )
