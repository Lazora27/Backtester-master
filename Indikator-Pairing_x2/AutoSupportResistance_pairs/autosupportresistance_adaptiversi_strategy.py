import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoSupportResistance_AdaptiveRSI_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoSupportResistance und AdaptiveRSI
    """
    
    params = (
        ('indicators', {
            'AutoSupportResistance': {
                'class': AutoSupportResistance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoSupportResistance'>
            },
            'AdaptiveRSI': {
                'class': AdaptiveRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveRSI'>
            }
        }),
        ('weights', {
            'AutoSupportResistance': 1.0,
            'AdaptiveRSI': 1.0
        })
    )
