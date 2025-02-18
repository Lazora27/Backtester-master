import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CVIRatio_VWAPDeviationBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CVIRatio und VWAPDeviationBands
    """
    
    params = (
        ('indicators', {
            'CVIRatio': {
                'class': CVIRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CVIRatio'>
            },
            'VWAPDeviationBands': {
                'class': VWAPDeviationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPDeviationBands'>
            }
        }),
        ('weights', {
            'CVIRatio': 1.0,
            'VWAPDeviationBands': 1.0
        })
    )
