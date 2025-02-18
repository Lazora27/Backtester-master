import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDPredictor_CoppockCurve_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDPredictor und CoppockCurve
    """
    
    params = (
        ('indicators', {
            'MACDPredictor': {
                'class': MACDPredictor,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDPredictor'>
            },
            'CoppockCurve': {
                'class': CoppockCurve,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CoppockCurve'>
            }
        }),
        ('weights', {
            'MACDPredictor': 1.0,
            'CoppockCurve': 1.0
        })
    )
