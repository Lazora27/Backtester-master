import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CVIRatio_AAIISentiment_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CVIRatio und AAIISentiment
    """
    
    params = (
        ('indicators', {
            'CVIRatio': {
                'class': CVIRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CVIRatio'>
            },
            'AAIISentiment': {
                'class': AAIISentiment,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AAIISentiment'>
            }
        }),
        ('weights', {
            'CVIRatio': 1.0,
            'AAIISentiment': 1.0
        })
    )
