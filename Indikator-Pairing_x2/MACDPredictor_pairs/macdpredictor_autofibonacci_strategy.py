import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDPredictor_AutoFibonacci_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDPredictor und AutoFibonacci
    """
    
    params = (
        ('indicators', {
            'MACDPredictor': {
                'class': MACDPredictor,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDPredictor'>
            },
            'AutoFibonacci': {
                'class': AutoFibonacci,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoFibonacci'>
            }
        }),
        ('weights', {
            'MACDPredictor': 1.0,
            'AutoFibonacci': 1.0
        })
    )
