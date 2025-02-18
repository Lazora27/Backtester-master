import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TapeReading_VWAPDeviationBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TapeReading und VWAPDeviationBands
    """
    
    params = (
        ('indicators', {
            'TapeReading': {
                'class': TapeReading,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TapeReading'>
            },
            'VWAPDeviationBands': {
                'class': VWAPDeviationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPDeviationBands'>
            }
        }),
        ('weights', {
            'TapeReading': 1.0,
            'VWAPDeviationBands': 1.0
        })
    )
