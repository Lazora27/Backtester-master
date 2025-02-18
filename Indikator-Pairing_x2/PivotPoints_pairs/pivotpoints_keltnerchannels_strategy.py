import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PivotPoints_KeltnerChannels_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PivotPoints und KeltnerChannels
    """
    
    params = (
        ('indicators', {
            'PivotPoints': {
                'class': PivotPoints,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PivotPoints'>
            },
            'KeltnerChannels': {
                'class': KeltnerChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerChannels'>
            }
        }),
        ('weights', {
            'PivotPoints': 1.0,
            'KeltnerChannels': 1.0
        })
    )
