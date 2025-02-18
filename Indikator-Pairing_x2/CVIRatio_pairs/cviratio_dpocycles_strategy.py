import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CVIRatio_DPOCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CVIRatio und DPOCycles
    """
    
    params = (
        ('indicators', {
            'CVIRatio': {
                'class': CVIRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CVIRatio'>
            },
            'DPOCycles': {
                'class': DPOCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DPOCycles'>
            }
        }),
        ('weights', {
            'CVIRatio': 1.0,
            'DPOCycles': 1.0
        })
    )
