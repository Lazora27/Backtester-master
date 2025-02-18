import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PivotPoints_DonchianChannels_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PivotPoints und DonchianChannels
    """
    
    params = (
        ('indicators', {
            'PivotPoints': {
                'class': PivotPoints,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PivotPoints'>
            },
            'DonchianChannels': {
                'class': DonchianChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianChannels'>
            }
        }),
        ('weights', {
            'PivotPoints': 1.0,
            'DonchianChannels': 1.0
        })
    )
