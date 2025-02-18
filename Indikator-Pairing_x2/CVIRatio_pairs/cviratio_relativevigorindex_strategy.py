import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CVIRatio_RelativeVigorIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CVIRatio und RelativeVigorIndex
    """
    
    params = (
        ('indicators', {
            'CVIRatio': {
                'class': CVIRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CVIRatio'>
            },
            'RelativeVigorIndex': {
                'class': RelativeVigorIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeVigorIndex'>
            }
        }),
        ('weights', {
            'CVIRatio': 1.0,
            'RelativeVigorIndex': 1.0
        })
    )
