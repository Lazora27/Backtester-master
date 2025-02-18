import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDPredictor_PivotPoints_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDPredictor und PivotPoints
    """
    
    params = (
        ('indicators', {
            'MACDPredictor': {
                'class': MACDPredictor,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDPredictor'>
            },
            'PivotPoints': {
                'class': PivotPoints,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PivotPoints'>
            }
        }),
        ('weights', {
            'MACDPredictor': 1.0,
            'PivotPoints': 1.0
        })
    )
