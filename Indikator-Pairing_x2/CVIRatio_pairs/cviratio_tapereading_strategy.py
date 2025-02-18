import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CVIRatio_TapeReading_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CVIRatio und TapeReading
    """
    
    params = (
        ('indicators', {
            'CVIRatio': {
                'class': CVIRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CVIRatio'>
            },
            'TapeReading': {
                'class': TapeReading,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TapeReading'>
            }
        }),
        ('weights', {
            'CVIRatio': 1.0,
            'TapeReading': 1.0
        })
    )
