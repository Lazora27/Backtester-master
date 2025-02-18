import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDPredictor_AverageLogRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDPredictor und AverageLogRange
    """
    
    params = (
        ('indicators', {
            'MACDPredictor': {
                'class': MACDPredictor,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDPredictor'>
            },
            'AverageLogRange': {
                'class': AverageLogRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageLogRange'>
            }
        }),
        ('weights', {
            'MACDPredictor': 1.0,
            'AverageLogRange': 1.0
        })
    )
