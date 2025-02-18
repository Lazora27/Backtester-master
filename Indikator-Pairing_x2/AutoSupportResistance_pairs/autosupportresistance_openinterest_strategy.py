import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoSupportResistance_OpenInterest_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoSupportResistance und OpenInterest
    """
    
    params = (
        ('indicators', {
            'AutoSupportResistance': {
                'class': AutoSupportResistance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoSupportResistance'>
            },
            'OpenInterest': {
                'class': OpenInterest,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OpenInterest'>
            }
        }),
        ('weights', {
            'AutoSupportResistance': 1.0,
            'OpenInterest': 1.0
        })
    )
