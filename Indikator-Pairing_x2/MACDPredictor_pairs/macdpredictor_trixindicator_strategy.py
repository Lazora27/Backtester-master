import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDPredictor_TRIXIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDPredictor und TRIXIndicator
    """
    
    params = (
        ('indicators', {
            'MACDPredictor': {
                'class': MACDPredictor,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDPredictor'>
            },
            'TRIXIndicator': {
                'class': TRIXIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TRIXIndicator'>
            }
        }),
        ('weights', {
            'MACDPredictor': 1.0,
            'TRIXIndicator': 1.0
        })
    )
