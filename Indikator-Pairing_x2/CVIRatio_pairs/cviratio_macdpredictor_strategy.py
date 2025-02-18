import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CVIRatio_MACDPredictor_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CVIRatio und MACDPredictor
    """
    
    params = (
        ('indicators', {
            'CVIRatio': {
                'class': CVIRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CVIRatio'>
            },
            'MACDPredictor': {
                'class': MACDPredictor,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDPredictor'>
            }
        }),
        ('weights', {
            'CVIRatio': 1.0,
            'MACDPredictor': 1.0
        })
    )
