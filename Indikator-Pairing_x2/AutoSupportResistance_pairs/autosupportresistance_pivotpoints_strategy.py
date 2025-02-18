import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoSupportResistance_PivotPoints_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoSupportResistance und PivotPoints
    """
    
    params = (
        ('indicators', {
            'AutoSupportResistance': {
                'class': AutoSupportResistance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoSupportResistance'>
            },
            'PivotPoints': {
                'class': PivotPoints,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PivotPoints'>
            }
        }),
        ('weights', {
            'AutoSupportResistance': 1.0,
            'PivotPoints': 1.0
        })
    )
