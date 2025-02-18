import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DeltaProfile_TickActivityIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DeltaProfile und TickActivityIndex
    """
    
    params = (
        ('indicators', {
            'DeltaProfile': {
                'class': DeltaProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DeltaProfile'>
            },
            'TickActivityIndex': {
                'class': TickActivityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickActivityIndex'>
            }
        }),
        ('weights', {
            'DeltaProfile': 1.0,
            'TickActivityIndex': 1.0
        })
    )
