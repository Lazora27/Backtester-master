import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TapeReading_ProjectionBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TapeReading und ProjectionBands
    """
    
    params = (
        ('indicators', {
            'TapeReading': {
                'class': TapeReading,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TapeReading'>
            },
            'ProjectionBands': {
                'class': ProjectionBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionBands'>
            }
        }),
        ('weights', {
            'TapeReading': 1.0,
            'ProjectionBands': 1.0
        })
    )
