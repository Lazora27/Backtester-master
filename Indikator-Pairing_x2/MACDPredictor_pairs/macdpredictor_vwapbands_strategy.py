import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDPredictor_VWAPBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDPredictor und VWAPBands
    """
    
    params = (
        ('indicators', {
            'MACDPredictor': {
                'class': MACDPredictor,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDPredictor'>
            },
            'VWAPBands': {
                'class': VWAPBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPBands'>
            }
        }),
        ('weights', {
            'MACDPredictor': 1.0,
            'VWAPBands': 1.0
        })
    )
