import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CVIRatio_DemandIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CVIRatio und DemandIndex
    """
    
    params = (
        ('indicators', {
            'CVIRatio': {
                'class': CVIRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CVIRatio'>
            },
            'DemandIndex': {
                'class': DemandIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandIndex'>
            }
        }),
        ('weights', {
            'CVIRatio': 1.0,
            'DemandIndex': 1.0
        })
    )
