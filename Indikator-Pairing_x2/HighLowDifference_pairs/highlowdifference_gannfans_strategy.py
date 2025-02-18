import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowDifference_GannFans_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowDifference und GannFans
    """
    
    params = (
        ('indicators', {
            'HighLowDifference': {
                'class': HighLowDifference,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowDifference'>
            },
            'GannFans': {
                'class': GannFans,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannFans'>
            }
        }),
        ('weights', {
            'HighLowDifference': 1.0,
            'GannFans': 1.0
        })
    )
