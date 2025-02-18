import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDPredictor_TapeReading_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDPredictor und TapeReading
    """
    
    params = (
        ('indicators', {
            'MACDPredictor': {
                'class': MACDPredictor,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDPredictor'>
            },
            'TapeReading': {
                'class': TapeReading,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TapeReading'>
            }
        }),
        ('weights', {
            'MACDPredictor': 1.0,
            'TapeReading': 1.0
        })
    )
