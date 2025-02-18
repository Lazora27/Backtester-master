import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickIndex_DeltaProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickIndex und DeltaProfile
    """
    
    params = (
        ('indicators', {
            'TickIndex': {
                'class': TickIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickIndex'>
            },
            'DeltaProfile': {
                'class': DeltaProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DeltaProfile'>
            }
        }),
        ('weights', {
            'TickIndex': 1.0,
            'DeltaProfile': 1.0
        })
    )
