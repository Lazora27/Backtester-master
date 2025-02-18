import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PutCallRatio_DeltaProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PutCallRatio und DeltaProfile
    """
    
    params = (
        ('indicators', {
            'PutCallRatio': {
                'class': PutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PutCallRatio1'>
            },
            'DeltaProfile': {
                'class': DeltaProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DeltaProfile'>
            }
        }),
        ('weights', {
            'PutCallRatio': 1.0,
            'DeltaProfile': 1.0
        })
    )
