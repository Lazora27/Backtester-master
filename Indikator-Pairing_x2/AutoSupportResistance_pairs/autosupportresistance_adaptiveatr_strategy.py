import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoSupportResistance_AdaptiveATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoSupportResistance und AdaptiveATR
    """
    
    params = (
        ('indicators', {
            'AutoSupportResistance': {
                'class': AutoSupportResistance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoSupportResistance'>
            },
            'AdaptiveATR': {
                'class': AdaptiveATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveATR'>
            }
        }),
        ('weights', {
            'AutoSupportResistance': 1.0,
            'AdaptiveATR': 1.0
        })
    )
