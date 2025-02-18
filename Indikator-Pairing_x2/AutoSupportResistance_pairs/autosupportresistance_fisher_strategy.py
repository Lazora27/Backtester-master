import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoSupportResistance_Fisher_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoSupportResistance und Fisher
    """
    
    params = (
        ('indicators', {
            'AutoSupportResistance': {
                'class': AutoSupportResistance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoSupportResistance'>
            },
            'Fisher': {
                'class': Fisher,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_Fisher'>
            }
        }),
        ('weights', {
            'AutoSupportResistance': 1.0,
            'Fisher': 1.0
        })
    )
