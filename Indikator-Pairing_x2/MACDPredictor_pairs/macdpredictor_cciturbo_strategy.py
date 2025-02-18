import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDPredictor_CCITurbo_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDPredictor und CCITurbo
    """
    
    params = (
        ('indicators', {
            'MACDPredictor': {
                'class': MACDPredictor,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDPredictor'>
            },
            'CCITurbo': {
                'class': CCITurbo,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CCITurbo'>
            }
        }),
        ('weights', {
            'MACDPredictor': 1.0,
            'CCITurbo': 1.0
        })
    )
