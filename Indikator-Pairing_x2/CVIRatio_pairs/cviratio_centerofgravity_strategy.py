import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CVIRatio_CenterOfGravity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CVIRatio und CenterOfGravity
    """
    
    params = (
        ('indicators', {
            'CVIRatio': {
                'class': CVIRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CVIRatio'>
            },
            'CenterOfGravity': {
                'class': CenterOfGravity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CenterOfGravity'>
            }
        }),
        ('weights', {
            'CVIRatio': 1.0,
            'CenterOfGravity': 1.0
        })
    )
