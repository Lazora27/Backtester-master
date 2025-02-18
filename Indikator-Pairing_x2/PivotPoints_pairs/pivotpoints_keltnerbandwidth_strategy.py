import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PivotPoints_KeltnerBandWidth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PivotPoints und KeltnerBandWidth
    """
    
    params = (
        ('indicators', {
            'PivotPoints': {
                'class': PivotPoints,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PivotPoints'>
            },
            'KeltnerBandWidth': {
                'class': KeltnerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerBandWidth'>
            }
        }),
        ('weights', {
            'PivotPoints': 1.0,
            'KeltnerBandWidth': 1.0
        })
    )
