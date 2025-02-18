import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoSupportResistance_MACDHistogram_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoSupportResistance und MACDHistogram
    """
    
    params = (
        ('indicators', {
            'AutoSupportResistance': {
                'class': AutoSupportResistance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoSupportResistance'>
            },
            'MACDHistogram': {
                'class': MACDHistogram,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDHistogram'>
            }
        }),
        ('weights', {
            'AutoSupportResistance': 1.0,
            'MACDHistogram': 1.0
        })
    )
