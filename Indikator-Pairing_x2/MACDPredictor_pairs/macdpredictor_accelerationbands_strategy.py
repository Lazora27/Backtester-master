import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDPredictor_AccelerationBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDPredictor und AccelerationBands
    """
    
    params = (
        ('indicators', {
            'MACDPredictor': {
                'class': MACDPredictor,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDPredictor'>
            },
            'AccelerationBands': {
                'class': AccelerationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccelerationBands'>
            }
        }),
        ('weights', {
            'MACDPredictor': 1.0,
            'AccelerationBands': 1.0
        })
    )
