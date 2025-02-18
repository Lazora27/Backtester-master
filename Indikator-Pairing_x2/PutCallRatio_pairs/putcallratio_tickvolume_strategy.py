import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PutCallRatio_TickVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PutCallRatio und TickVolume
    """
    
    params = (
        ('indicators', {
            'PutCallRatio': {
                'class': PutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PutCallRatio1'>
            },
            'TickVolume': {
                'class': TickVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickVolume'>
            }
        }),
        ('weights', {
            'PutCallRatio': 1.0,
            'TickVolume': 1.0
        })
    )
