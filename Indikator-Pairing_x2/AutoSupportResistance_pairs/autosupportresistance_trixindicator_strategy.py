import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoSupportResistance_TRIXIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoSupportResistance und TRIXIndicator
    """
    
    params = (
        ('indicators', {
            'AutoSupportResistance': {
                'class': AutoSupportResistance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoSupportResistance'>
            },
            'TRIXIndicator': {
                'class': TRIXIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TRIXIndicator'>
            }
        }),
        ('weights', {
            'AutoSupportResistance': 1.0,
            'TRIXIndicator': 1.0
        })
    )
