import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoSupportResistance_ModifiedRSI_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoSupportResistance und ModifiedRSI
    """
    
    params = (
        ('indicators', {
            'AutoSupportResistance': {
                'class': AutoSupportResistance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoSupportResistance'>
            },
            'ModifiedRSI': {
                'class': ModifiedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedRSI'>
            }
        }),
        ('weights', {
            'AutoSupportResistance': 1.0,
            'ModifiedRSI': 1.0
        })
    )
