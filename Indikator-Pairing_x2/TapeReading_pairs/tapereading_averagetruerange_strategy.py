import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TapeReading_AverageTrueRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TapeReading und AverageTrueRange
    """
    
    params = (
        ('indicators', {
            'TapeReading': {
                'class': TapeReading,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TapeReading'>
            },
            'AverageTrueRange': {
                'class': AverageTrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageTrueRange1'>
            }
        }),
        ('weights', {
            'TapeReading': 1.0,
            'AverageTrueRange': 1.0
        })
    )
