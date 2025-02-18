import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PivotPoints_TradeVolumeIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PivotPoints und TradeVolumeIndex
    """
    
    params = (
        ('indicators', {
            'PivotPoints': {
                'class': PivotPoints,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PivotPoints'>
            },
            'TradeVolumeIndex': {
                'class': TradeVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TradeVolumeIndex'>
            }
        }),
        ('weights', {
            'PivotPoints': 1.0,
            'TradeVolumeIndex': 1.0
        })
    )
