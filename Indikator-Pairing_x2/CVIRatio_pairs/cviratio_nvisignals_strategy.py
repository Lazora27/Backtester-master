import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CVIRatio_NVISignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CVIRatio und NVISignals
    """
    
    params = (
        ('indicators', {
            'CVIRatio': {
                'class': CVIRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CVIRatio'>
            },
            'NVISignals': {
                'class': NVISignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NVISignals'>
            }
        }),
        ('weights', {
            'CVIRatio': 1.0,
            'NVISignals': 1.0
        })
    )
