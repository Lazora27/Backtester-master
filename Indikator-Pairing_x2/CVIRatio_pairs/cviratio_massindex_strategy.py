import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CVIRatio_MassIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CVIRatio und MassIndex
    """
    
    params = (
        ('indicators', {
            'CVIRatio': {
                'class': CVIRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CVIRatio'>
            },
            'MassIndex': {
                'class': MassIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MassIndex'>
            }
        }),
        ('weights', {
            'CVIRatio': 1.0,
            'MassIndex': 1.0
        })
    )
