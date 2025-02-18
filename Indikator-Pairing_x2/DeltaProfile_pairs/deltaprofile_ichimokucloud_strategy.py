import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DeltaProfile_IchimokuCloud_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DeltaProfile und IchimokuCloud
    """
    
    params = (
        ('indicators', {
            'DeltaProfile': {
                'class': DeltaProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DeltaProfile'>
            },
            'IchimokuCloud': {
                'class': IchimokuCloud,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IchimokuCloud'>
            }
        }),
        ('weights', {
            'DeltaProfile': 1.0,
            'IchimokuCloud': 1.0
        })
    )
