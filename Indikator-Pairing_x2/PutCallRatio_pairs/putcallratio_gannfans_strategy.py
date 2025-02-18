import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PutCallRatio_GannFans_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PutCallRatio und GannFans
    """
    
    params = (
        ('indicators', {
            'PutCallRatio': {
                'class': PutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PutCallRatio1'>
            },
            'GannFans': {
                'class': GannFans,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannFans'>
            }
        }),
        ('weights', {
            'PutCallRatio': 1.0,
            'GannFans': 1.0
        })
    )
