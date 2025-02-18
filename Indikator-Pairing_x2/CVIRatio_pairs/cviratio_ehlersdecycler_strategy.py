import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CVIRatio_EhlersDecycler_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CVIRatio und EhlersDecycler
    """
    
    params = (
        ('indicators', {
            'CVIRatio': {
                'class': CVIRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CVIRatio'>
            },
            'EhlersDecycler': {
                'class': EhlersDecycler,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersDecycler'>
            }
        }),
        ('weights', {
            'CVIRatio': 1.0,
            'EhlersDecycler': 1.0
        })
    )
