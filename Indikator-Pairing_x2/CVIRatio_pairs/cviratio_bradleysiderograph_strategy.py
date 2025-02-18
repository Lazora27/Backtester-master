import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CVIRatio_BradleySiderograph_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CVIRatio und BradleySiderograph
    """
    
    params = (
        ('indicators', {
            'CVIRatio': {
                'class': CVIRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CVIRatio'>
            },
            'BradleySiderograph': {
                'class': BradleySiderograph,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BradleySiderograph'>
            }
        }),
        ('weights', {
            'CVIRatio': 1.0,
            'BradleySiderograph': 1.0
        })
    )
