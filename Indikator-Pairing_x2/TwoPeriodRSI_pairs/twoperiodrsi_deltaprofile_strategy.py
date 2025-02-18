import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TwoPeriodRSI_DeltaProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TwoPeriodRSI und DeltaProfile
    """
    
    params = (
        ('indicators', {
            'TwoPeriodRSI': {
                'class': TwoPeriodRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TwoPeriodRSI'>
            },
            'DeltaProfile': {
                'class': DeltaProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DeltaProfile'>
            }
        }),
        ('weights', {
            'TwoPeriodRSI': 1.0,
            'DeltaProfile': 1.0
        })
    )
