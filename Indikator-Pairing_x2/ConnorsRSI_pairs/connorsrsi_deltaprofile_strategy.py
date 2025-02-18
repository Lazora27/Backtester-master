import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ConnorsRSI_DeltaProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ConnorsRSI und DeltaProfile
    """
    
    params = (
        ('indicators', {
            'ConnorsRSI': {
                'class': ConnorsRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ConnorsRSI'>
            },
            'DeltaProfile': {
                'class': DeltaProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DeltaProfile'>
            }
        }),
        ('weights', {
            'ConnorsRSI': 1.0,
            'DeltaProfile': 1.0
        })
    )
