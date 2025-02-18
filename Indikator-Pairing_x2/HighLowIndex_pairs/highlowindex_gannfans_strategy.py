import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowIndex_GannFans_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowIndex und GannFans
    """
    
    params = (
        ('indicators', {
            'HighLowIndex': {
                'class': HighLowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowIndex'>
            },
            'GannFans': {
                'class': GannFans,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannFans'>
            }
        }),
        ('weights', {
            'HighLowIndex': 1.0,
            'GannFans': 1.0
        })
    )
