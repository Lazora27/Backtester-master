import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ModifiedRSI_TapeReading_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ModifiedRSI und TapeReading
    """
    
    params = (
        ('indicators', {
            'ModifiedRSI': {
                'class': ModifiedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedRSI'>
            },
            'TapeReading': {
                'class': TapeReading,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TapeReading'>
            }
        }),
        ('weights', {
            'ModifiedRSI': 1.0,
            'TapeReading': 1.0
        })
    )
