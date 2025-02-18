import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDPredictor_TrueRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDPredictor und TrueRange
    """
    
    params = (
        ('indicators', {
            'MACDPredictor': {
                'class': MACDPredictor,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDPredictor'>
            },
            'TrueRange': {
                'class': TrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRange1'>
            }
        }),
        ('weights', {
            'MACDPredictor': 1.0,
            'TrueRange': 1.0
        })
    )
