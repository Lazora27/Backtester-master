import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CVIRatio_CCITurbo_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CVIRatio und CCITurbo
    """
    
    params = (
        ('indicators', {
            'CVIRatio': {
                'class': CVIRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CVIRatio'>
            },
            'CCITurbo': {
                'class': CCITurbo,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CCITurbo'>
            }
        }),
        ('weights', {
            'CVIRatio': 1.0,
            'CCITurbo': 1.0
        })
    )
