import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DeltaProfile_ChandeKrollStop_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DeltaProfile und ChandeKrollStop
    """
    
    params = (
        ('indicators', {
            'DeltaProfile': {
                'class': DeltaProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DeltaProfile'>
            },
            'ChandeKrollStop': {
                'class': ChandeKrollStop,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeKrollStop'>
            }
        }),
        ('weights', {
            'DeltaProfile': 1.0,
            'ChandeKrollStop': 1.0
        })
    )
