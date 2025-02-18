import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDPredictor_ModifiedATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDPredictor und ModifiedATR
    """
    
    params = (
        ('indicators', {
            'MACDPredictor': {
                'class': MACDPredictor,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDPredictor'>
            },
            'ModifiedATR': {
                'class': ModifiedATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedATR'>
            }
        }),
        ('weights', {
            'MACDPredictor': 1.0,
            'ModifiedATR': 1.0
        })
    )
