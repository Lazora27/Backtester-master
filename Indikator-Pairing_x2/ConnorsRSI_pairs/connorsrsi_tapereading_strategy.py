import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ConnorsRSI_TapeReading_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ConnorsRSI und TapeReading
    """
    
    params = (
        ('indicators', {
            'ConnorsRSI': {
                'class': ConnorsRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ConnorsRSI'>
            },
            'TapeReading': {
                'class': TapeReading,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TapeReading'>
            }
        }),
        ('weights', {
            'ConnorsRSI': 1.0,
            'TapeReading': 1.0
        })
    )
