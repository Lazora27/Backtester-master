import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TapeReading_ProjectionOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TapeReading und ProjectionOscillator
    """
    
    params = (
        ('indicators', {
            'TapeReading': {
                'class': TapeReading,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TapeReading'>
            },
            'ProjectionOscillator': {
                'class': ProjectionOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionOscillator'>
            }
        }),
        ('weights', {
            'TapeReading': 1.0,
            'ProjectionOscillator': 1.0
        })
    )
