import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CVIRatio_EldersForceIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CVIRatio und EldersForceIndex
    """
    
    params = (
        ('indicators', {
            'CVIRatio': {
                'class': CVIRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CVIRatio'>
            },
            'EldersForceIndex': {
                'class': EldersForceIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EldersForceIndex'>
            }
        }),
        ('weights', {
            'CVIRatio': 1.0,
            'EldersForceIndex': 1.0
        })
    )
