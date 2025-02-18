import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDPredictor_SuperTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDPredictor und SuperTrend
    """
    
    params = (
        ('indicators', {
            'MACDPredictor': {
                'class': MACDPredictor,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDPredictor'>
            },
            'SuperTrend': {
                'class': SuperTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperTrend'>
            }
        }),
        ('weights', {
            'MACDPredictor': 1.0,
            'SuperTrend': 1.0
        })
    )
