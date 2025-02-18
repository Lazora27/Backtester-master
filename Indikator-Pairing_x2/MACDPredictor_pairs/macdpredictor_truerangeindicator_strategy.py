import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDPredictor_TrueRangeIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDPredictor und TrueRangeIndicator
    """
    
    params = (
        ('indicators', {
            'MACDPredictor': {
                'class': MACDPredictor,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDPredictor'>
            },
            'TrueRangeIndicator': {
                'class': TrueRangeIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRangeIndicator'>
            }
        }),
        ('weights', {
            'MACDPredictor': 1.0,
            'TrueRangeIndicator': 1.0
        })
    )
