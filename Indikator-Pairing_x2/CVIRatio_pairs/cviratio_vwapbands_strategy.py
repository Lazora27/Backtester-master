import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CVIRatio_VWAPBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CVIRatio und VWAPBands
    """
    
    params = (
        ('indicators', {
            'CVIRatio': {
                'class': CVIRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CVIRatio'>
            },
            'VWAPBands': {
                'class': VWAPBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPBands'>
            }
        }),
        ('weights', {
            'CVIRatio': 1.0,
            'VWAPBands': 1.0
        })
    )
