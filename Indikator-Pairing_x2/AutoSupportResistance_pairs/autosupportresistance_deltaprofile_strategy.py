import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoSupportResistance_DeltaProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoSupportResistance und DeltaProfile
    """
    
    params = (
        ('indicators', {
            'AutoSupportResistance': {
                'class': AutoSupportResistance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoSupportResistance'>
            },
            'DeltaProfile': {
                'class': DeltaProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DeltaProfile'>
            }
        }),
        ('weights', {
            'AutoSupportResistance': 1.0,
            'DeltaProfile': 1.0
        })
    )
