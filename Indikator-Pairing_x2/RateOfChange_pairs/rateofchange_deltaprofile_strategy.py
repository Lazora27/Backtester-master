import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RateOfChange_DeltaProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RateOfChange und DeltaProfile
    """
    
    params = (
        ('indicators', {
            'RateOfChange': {
                'class': RateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RateOfChange1'>
            },
            'DeltaProfile': {
                'class': DeltaProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DeltaProfile'>
            }
        }),
        ('weights', {
            'RateOfChange': 1.0,
            'DeltaProfile': 1.0
        })
    )
