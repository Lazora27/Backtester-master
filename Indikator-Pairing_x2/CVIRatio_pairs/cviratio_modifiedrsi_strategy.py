import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CVIRatio_ModifiedRSI_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CVIRatio und ModifiedRSI
    """
    
    params = (
        ('indicators', {
            'CVIRatio': {
                'class': CVIRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CVIRatio'>
            },
            'ModifiedRSI': {
                'class': ModifiedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedRSI'>
            }
        }),
        ('weights', {
            'CVIRatio': 1.0,
            'ModifiedRSI': 1.0
        })
    )
