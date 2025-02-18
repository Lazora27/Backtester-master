import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoSupportResistance_HighLowDifference_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoSupportResistance und HighLowDifference
    """
    
    params = (
        ('indicators', {
            'AutoSupportResistance': {
                'class': AutoSupportResistance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoSupportResistance'>
            },
            'HighLowDifference': {
                'class': HighLowDifference,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowDifference'>
            }
        }),
        ('weights', {
            'AutoSupportResistance': 1.0,
            'HighLowDifference': 1.0
        })
    )
