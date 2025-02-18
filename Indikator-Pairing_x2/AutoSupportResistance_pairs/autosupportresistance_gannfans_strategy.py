import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoSupportResistance_GannFans_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoSupportResistance und GannFans
    """
    
    params = (
        ('indicators', {
            'AutoSupportResistance': {
                'class': AutoSupportResistance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoSupportResistance'>
            },
            'GannFans': {
                'class': GannFans,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannFans'>
            }
        }),
        ('weights', {
            'AutoSupportResistance': 1.0,
            'GannFans': 1.0
        })
    )
